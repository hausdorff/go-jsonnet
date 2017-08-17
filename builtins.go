/*
Copyright 2017 Google Inc. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package jsonnet

// TODO(sbarzowski) Is this the best option? It's the first one that worked for me...
//go:generate esc -o std.go -pkg=jsonnet std/std.jsonnet

func getStdCode() string {
	return FSMustString(false, "/std/std.jsonnet")
}

func builtinPlus(e *evaluator, xp, yp potentialValue) (value, error) {
	// TODO(sbarzowski) more types, mixing types
	// TODO(sbarzowski) perhaps a more elegant way to dispatch
	x, err := e.evaluate(xp)
	if err != nil {
		return nil, err
	}
	switch left := x.(type) {
	case *valueNumber:
		right, err := e.evaluateNumber(yp)
		if err != nil {
			return nil, err
		}
		return makeValueNumber(left.value + right.value), nil
	case *valueString:
		right, err := e.evaluateString(yp)
		if err != nil {
			return nil, err
		}
		return makeValueString(left.value + right.value), nil
	case valueObject:
		right, err := e.evaluateObject(yp)
		if err != nil {
			return nil, err
		}
		return makeValueExtendedObject(left, right), nil
	default:
		return nil, e.typeErrorGeneral(x)
	}
}

func builtinMinus(e *evaluator, xp, yp potentialValue) (value, error) {
	x, err := e.evaluateNumber(xp)
	if err != nil {
		return nil, err
	}
	y, err := e.evaluateNumber(yp)
	if err != nil {
		return nil, err
	}
	return makeValueNumber(x.value - y.value), nil
}

func builtinGreater(e *evaluator, xp, yp potentialValue) (value, error) {
	x, err := e.evaluate(xp)
	if err != nil {
		return nil, err
	}
	switch left := x.(type) {
	case *valueNumber:
		right, err := e.evaluateNumber(yp)
		if err != nil {
			return nil, err
		}
		return makeValueBoolean(left.value > right.value), nil
	case *valueString:
		right, err := e.evaluateString(yp)
		if err != nil {
			return nil, err
		}
		return makeValueBoolean(left.value > right.value), nil
	default:
		return nil, e.typeErrorGeneral(x)
	}
}

func builtinLess(e *evaluator, xp, yp potentialValue) (value, error) {
	return builtinGreater(e, yp, xp)
}

func builtinGreaterEq(e *evaluator, xp, yp potentialValue) (value, error) {
	res, err := builtinLess(e, xp, yp)
	if err != nil {
		return nil, err
	}
	return res.(*valueBoolean).not(), nil
}

func builtinLessEq(e *evaluator, xp, yp potentialValue) (value, error) {
	res, err := builtinGreater(e, xp, yp)
	if err != nil {
		return nil, err
	}
	return res.(*valueBoolean).not(), nil
}

func builtinAnd(e *evaluator, xp, yp potentialValue) (value, error) {
	x, err := e.evaluateBoolean(xp)
	if err != nil {
		return nil, err
	}
	if !x.value {
		return x, nil
	}
	y, err := e.evaluateBoolean(yp)
	if err != nil {
		return nil, err
	}
	return y, nil
}

func builtinLength(e *evaluator, xp potentialValue) (value, error) {
	x, err := e.evaluate(xp)
	if err != nil {
		return nil, err
	}
	var num int
	switch x := x.(type) {
	case *valueSimpleObject:
		panic("TODO getting all the fields")
	case *valueArray:
		num = len(x.elements)
	case *valueString:
		num = len(x.value)
	case *valueFunction:
		num = len(x.parameters())
	default:
		return nil, e.typeErrorGeneral(x)
	}
	return makeValueNumber(float64(num)), nil
}

func builtinMakeArray(e *evaluator, szp potentialValue, funcp potentialValue) (value, error) {
	sz, err := e.evaluateNumber(szp)
	if err != nil {
		return nil, err
	}
	fun, err := e.evaluateFunction(funcp)
	if err != nil {
		return nil, err
	}
	num := int(sz.value)
	var elems []potentialValue
	for i := 0; i < num; i++ {
		elem := fun.call(args(&readyValue{intToValue(i)}))
		elems = append(elems, elem)
	}
	return makeValueArray(elems), nil
}

func builtinNegation(e *evaluator, xp potentialValue) (value, error) {
	x, err := e.evaluateBoolean(xp)
	if err != nil {
		return nil, err
	}
	return makeValueBoolean(!x.value), nil
}

func builtinBitNeg(e *evaluator, xp potentialValue) (value, error) {
	x, err := e.evaluateNumber(xp)
	if err != nil {
		return nil, err
	}
	i := int64(x.value)
	return int64ToValue(^i), nil
}

func builtinIdentity(e *evaluator, xp potentialValue) (value, error) {
	x, err := e.evaluate(xp)
	if err != nil {
		return nil, err
	}
	return x, nil
}

func builtinUnaryMinus(e *evaluator, xp potentialValue) (value, error) {
	x, err := e.evaluateNumber(xp)
	if err != nil {
		return nil, err
	}
	return makeValueNumber(-x.value), nil
}

func primitiveEquals(e *evaluator, xp potentialValue, yp potentialValue) (value, error) {
	x, err := e.evaluate(xp)
	if err != nil {
		return nil, err
	}
	y, err := e.evaluate(yp)
	if err != nil {
		return nil, err
	}
	if x.typename() != y.typename() { // TODO(sbarzowski) ugh, string comparison
		return makeValueBoolean(false), nil
	}
	switch left := x.(type) {
	case *valueBoolean:
		right, err := e.getBoolean(y)
		if err != nil {
			return nil, err
		}
		return makeValueBoolean(left.value == right.value), nil
	case *valueNumber:
		right, err := e.getNumber(y)
		if err != nil {
			return nil, err
		}
		return makeValueBoolean(left.value == right.value), nil
	case *valueString:
		right, err := e.getString(y)
		if err != nil {
			return nil, err
		}
		return makeValueBoolean(left.value == right.value), nil
	case *valueNull:
		return makeValueBoolean(true), nil
	case *valueFunction:
		return nil, e.Error("Cannot test equality of functions")
	default:
		return nil, e.Error(
			"primitiveEquals operates on primitive types, got " + x.typename(),
		)
	}
}

func builtinType(e *evaluator, xp potentialValue) (value, error) {
	x, err := e.evaluate(xp)
	if err != nil {
		return nil, err
	}
	return makeValueString(x.typename()), nil
}

type unaryBuiltin func(*evaluator, potentialValue) (value, error)
type binaryBuiltin func(*evaluator, potentialValue, potentialValue) (value, error)

type UnaryBuiltin struct {
	name       Identifier
	function   unaryBuiltin
	parameters Identifiers
}

func getBuiltinEvaluator(e *evaluator, name Identifier) *evaluator {
	loc := makeLocationRangeMessage("<builtin>")
	context := TraceContext{Name: "builtin function <" + string(name) + ">"}
	trace := TraceElement{loc: &loc, context: &context}
	return &evaluator{i: e.i, trace: &trace}
}

func (b *UnaryBuiltin) EvalCall(args callArguments, e *evaluator) (value, error) {

	// TODO check args
	return b.function(getBuiltinEvaluator(e, b.name), args.positional[0])
}

func (b *UnaryBuiltin) Parameters() Identifiers {
	return b.parameters
}

type BinaryBuiltin struct {
	name       Identifier
	function   binaryBuiltin
	parameters Identifiers
}

func (b *BinaryBuiltin) EvalCall(args callArguments, e *evaluator) (value, error) {
	// TODO check args
	return b.function(getBuiltinEvaluator(e, b.name), args.positional[0], args.positional[1])
}

func (b *BinaryBuiltin) Parameters() Identifiers {
	return b.parameters
}

func todoFunc(e *evaluator, x, y potentialValue) (value, error) {
	return nil, e.Error("not implemented yet")
}

// so that we don't get segfaults
var todo = &BinaryBuiltin{function: todoFunc, parameters: Identifiers{"x", "y"}}

var desugaredBop = map[BinaryOp]Identifier{
	//bopPercent,
	BopManifestEqual:   "equals",
	BopManifestUnequal: "notEquals", // Special case
}

var bopBuiltins = []*BinaryBuiltin{
	BopMult:    todo,
	BopDiv:     todo,
	BopPercent: todo,

	BopPlus:  &BinaryBuiltin{name: "operator+", function: builtinPlus, parameters: Identifiers{"x", "y"}},
	BopMinus: &BinaryBuiltin{name: "operator-", function: builtinMinus, parameters: Identifiers{"x", "y"}},

	BopShiftL: todo,
	BopShiftR: todo,

	BopGreater:   &BinaryBuiltin{name: "operator>", function: builtinGreater, parameters: Identifiers{"x", "y"}},
	BopGreaterEq: &BinaryBuiltin{name: "operator>=", function: builtinGreaterEq, parameters: Identifiers{"x", "y"}},
	BopLess:      &BinaryBuiltin{name: "operator<,", function: builtinLess, parameters: Identifiers{"x", "y"}},
	BopLessEq:    &BinaryBuiltin{name: "operator<=", function: builtinLessEq, parameters: Identifiers{"x", "y"}},

	BopManifestEqual:   todo,
	BopManifestUnequal: todo,

	BopBitwiseAnd: todo,
	BopBitwiseXor: todo,
	BopBitwiseOr:  todo,

	BopAnd: &BinaryBuiltin{name: "operator&&", function: builtinAnd, parameters: Identifiers{"x", "y"}},
	BopOr:  todo,
}

var uopBuiltins = []*UnaryBuiltin{
	UopNot:        &UnaryBuiltin{name: "operator!", function: builtinNegation, parameters: Identifiers{"x"}},
	UopBitwiseNot: &UnaryBuiltin{name: "operator~", function: builtinBitNeg, parameters: Identifiers{"x"}},
	UopPlus:       &UnaryBuiltin{name: "operator+ (unary)", function: builtinIdentity, parameters: Identifiers{"x"}},
	UopMinus:      &UnaryBuiltin{name: "operator- (unary)", function: builtinUnaryMinus, parameters: Identifiers{"x"}},
}

// TODO(sbarzowski) eliminate duplication in function names (e.g. build map from array or constants)
var funcBuiltins = map[string]evalCallable{
	"length":          &UnaryBuiltin{name: "length", function: builtinLength, parameters: Identifiers{"x"}},
	"makeArray":       &BinaryBuiltin{name: "makeArray", function: builtinMakeArray, parameters: Identifiers{"sz", "func"}},
	"primitiveEquals": &BinaryBuiltin{name: "primitiveEquals", function: primitiveEquals, parameters: Identifiers{"sz", "func"}},
	"type":            &UnaryBuiltin{name: "type", function: builtinType, parameters: Identifiers{"x"}},
}
