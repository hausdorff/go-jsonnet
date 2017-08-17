from subprocess import call

ids = [
  # ("identifier", "Identifier"),
  # ("identifiers", "Identifiers"),
  # ("astNode", "Node"),
  # ("astNodes", "Nodes"),
  # ("astNodeBase", "nodeBase"),
  # ("astCompKind", "CompKind"),
  # ("astCompFor", "CompFor"),
  # ("astCompIf", "CompIf"),

  # ("astCompSpec.kind", "Kind"),
  # ("astCompSpec.varName", "VarName"),
  # ("astCompSpec.expr", "Expr"),
  # ("astCompSpec", "CompSpec"),
  # ("astCompSpecs", "CompSpecs"),

  # ("astApply.target", "Target"),
  # ("astApply.arguments", "Arguments"),
  # ("astApply.trailingComma", "TrailingComma"),
  # ("astApply.tailStrict", "TailStrict"),
  # ("astApply", "Apply"),

  # ("astApplyBrace.left", "Left"),
  # ("astApplyBrace.right", "Right"),
  # ("astApplyBrace", "ApplyBrace"),

  # ("astArray.elements", "Elements"),
  # ("astArray.trailingComma", "TrailingComma"),
  # ("astArray", "Array"),

  # ("astArrayComp.body", "Body"),
  # ("astArrayComp.trailingComma", "TrailingComma"),
  # ("astArrayComp.specs", "Specs"),
  # ("astArrayComp", "ArrayComp"),

  # ("astAssert.cond", "Cond"),
  # ("astAssert.message", "Message"),
  # ("astAssert.rest", "Rest"),
  # ("astAssert", "Assert"),

  # ("binaryOp", "BinaryOp"),
  # ("bopMult", "BopMult"),
  # ("bopDiv", "BopDiv"),
  # ("bopPercent", "BopPercent"),
  # ("bopPlus", "BopPlus"),
  # ("bopMinus", "BopMinus"),
  # ("bopShiftL", "BopShiftL"),
  # ("bopShiftR", "BopShiftR"),
  # ("bopGreater", "BopGreater"),
  # ("bopGreaterEq", "BopGreaterEq"),
  # ("bopLess", "BopLess"),
  # ("bopLessEq", "BopLessEq"),
  # ("bopManifestEqual", "BopManifestEqual"),
  # ("bopManifestUnequal", "BopManifestUnequal"),
  # ("bopBitwiseAnd", "BopBitwiseAnd"),
  # ("bopBitwiseXor", "BopBitwiseXor"),
  # ("bopBitwiseOr", "BopBitwiseOr"),
  # ("bopAnd", "BopAnd"),
  # ("bopOr", "BopOr"),

  # ("astBinary.left", "Left"),
  # ("astBinary.op", "Op"),
  # ("astBinary.right", "Right"),
  # ("astBinary", "Binary"),

  # ("astConditional.cond", "Cond"),
  # ("astConditional.branchTrue", "BranchTrue"),
  # ("astConditional.branchFalse", "BranchFalse"),
  # ("astConditional", "Conditional"),

  # ("astDollar", "Dollar"),

  # ("astError.expr", "Expr"),
  # ("astError", "Error"),

  # ("astFunction.parameters", "Parameters"),
  # ("astFunction.trailingComma", "TrailingComma"),
  # ("astFunction.body", "Body"),
  # ("astFunction", "Function"),

  # ("astImport.file", "File"),
  # ("astImport", "Import"),

  # ("astImportStr.file", "File"),
  # ("astImportStr", "ImportStr"),

  # ("astIndex.target", "Target"),
  # ("astIndex.index", "Index"),
  # ("astIndex.id", "Id"),
  # ("astIndex", "Index"),

  # ("astSlice.target", "Target"),
  # ("astSlice.beginIndex", "BeginIndex"),
  # ("astSlice.endIndex", "EndIndex"),
  # ("astSlice.step", "Step"),
  # ("astSlice", "Slice"),

  # ("astLocalBind.variable", "Variable"),
  # ("astLocalBind.body", "Body"),
  # ("astLocalBind.functionSugar", "FunctionSugar"),
  # ("astLocalBind.params", "Params"),
  # ("astLocalBind.trailingComma", "TrailingComma"),
  # ("astLocalBind", "LocalBind"),
  # ("astLocalBinds", "LocalBinds"),

  # ("astLocal.binds", "Binds"),
  # ("astLocal.body", "Body"),
  # ("astLocal", "Local"),

  # ("astLiteralBoolean.value", "Value"),
  # ("astLiteralBoolean", "LiteralBoolean"),

  # ("astLiteralNull", "LiteralNull"),

  # ("astLiteralNumber.value", "Value"),
  # ("astLiteralNumber.originalString", "OriginalString"),
  # ("astLiteralNumber", "LiteralNumber"),

  # ("astLiteralStringKind", "LiteralStringKind"),
  # ("astStringSingle", "StringSingle"),
  # ("astStringDouble", "StringDouble"),
  # ("astStringBlock", "StringBlock"),
  # ("astVerbatimStringDouble", "VerbatimStringDouble"),
  # ("astVerbatimStringSingle", "VerbatimStringSingle"),

  # ("astLiteralString.value", "Value"),
  # ("astLiteralString.kind", "Kind"),
  # ("astLiteralString.blockIndent", "BlockIndent"),
  # ("astLiteralString", "LiteralString"),

  # ("astObjectFieldKind", "ObjectFieldKind"),
  # ("astObjectAssert", "ObjectAssert"),
  # ("astObjectFieldID", "ObjectFieldID"),
  # ("astObjectFieldExpr", "ObjectFieldExpr"),
  # ("astObjectFieldStr", "ObjectFieldStr"),
  # ("astObjectLocal", "ObjectLocal"),

  # ("astObjectFieldHide", "ObjectFieldHide"),
  # ("astObjectFieldHidden", "ObjectFieldHidden"),
  # ("astObjectFieldInherit", "ObjectFieldInherit"),
  # ("astObjectFieldVisible", "ObjectFieldVisible"),

  # ("astObjectField.kind", "Kind"),
  # ("astObjectField.hide", "Hide"),
  # ("astObjectField.superSugar", "SuperSugar"),
  # ("astObjectField.methodSugar", "MethodSugar"),
  # ("astObjectField.expr1", "Expr1"),
  # ("astObjectField.id", "Id"),
  # ("astObjectField.ids", "Ids"),
  # ("astObjectField.trailingComma", "TrailingComma"),
  # ("astObjectField.expr2", "Expr2"),
  # ("astObjectField.expr3", "Expr3"),
  # ("astObjectField", "ObjectField"),
  # ("astObjectFields", "ObjectFields"),

  # ("astObjectFieldLocal", "ObjectFieldLocal"),
  # ("astObjectFieldLocalNoMethod", "ObjectFieldLocalNoMethod"),

  # ("astObject.fields", "Fields"),
  # ("astObject.trailingComma", "TrailingComma"),
  # ("astObject", "Object"),

  # ("astDesugaredObjectField.hide", "Hide"),
  # ("astDesugaredObjectField.name", "Name"),
  # ("astDesugaredObjectField.body", "Body"),
  # ("astDesugaredObjectField", "DesugaredObjectField"),
  # ("astDesugaredObjectFields", "DesugaredObjectFields"),

  # ("astDesugaredObject.asserts", "Asserts"),
  # ("astDesugaredObject.fields", "Fields"),
  # ("astDesugaredObject", "DesugaredObject"),

  # ("astObjectComp.fields", "Fields"),
  # ("astObjectComp.trailingComma", "TrailingComma"),
  # ("astObjectComp.specs", "Specs"),
  # ("astObjectComp", "ObjectComp"),

  # ("astObjectComprehensionSimple.field", "Field"),
  # ("astObjectComprehensionSimple.value", "Value"),
  # ("astObjectComprehensionSimple.id", "Id"),
  # ("astObjectComprehensionSimple.array", "Array"),
  # ("astObjectComprehensionSimple", "ObjectComprehensionSimple"),

  # ("astSelf", "Self"),

  # ("astSuperIndex.index", "Index"),
  # ("astSuperIndex.id", "Id"),
  # ("astSuperIndex", "SuperIndex"),

  # ("unaryOp", "UnaryOp"),
  # ("uopNot", "UopNot"),
  # ("uopBitwiseNot", "UopBitwiseNot"),
  # ("uopPlus", "UopPlus"),
  # ("uopMinus", "UopMinus"),

  # ("astUnary.op", "Op"),
  # ("astUnary.expr", "Expr"),
  # ("astUnary", "Unary"),

  # ("astVar.id", "Id"),
  # ("astVar", "Var"),

  # ("fodderKind", "FodderKind"),
  # ("fodderWhitespace", "FodderWhitespace"),
  # ("fodderCommentC", "FodderCommentC"),
  # ("fodderCommentCpp", "FodderCommentCpp"),
  # ("fodderCommentHash", "FodderCommentHash"),

  # ("fodderElement.kind", "Kind"),
  # ("fodderElement.data", "Data"),
  # ("fodderElement", "FodderElement"),

  # ("fodder", "Fodder"),

  # ("tokenKind", "TokenKind"),
  # ("tokenBraceL", "TokenBraceL"),
  # ("tokenBraceR", "TokenBraceR"),
  # ("tokenBracketL", "TokenBracketL"),
  # ("tokenBracketR", "TokenBracketR"),
  # ("tokenComma", "TokenComma"),
  # ("tokenDollar", "TokenDollar"),
  # ("tokenDot", "TokenDot"),
  # ("tokenParenL", "TokenParenL"),
  # ("tokenParenR", "TokenParenR"),
  # ("tokenSemicolon", "TokenSemicolon"),

  # ("tokenIdentifier", "TokenIdentifier"),
  # ("tokenNumber", "TokenNumber"),
  # ("tokenOperator", "TokenOperator"),
  # ("tokenStringBlock", "TokenStringBlock"),
  # ("tokenStringDouble", "TokenStringDouble"),
  # ("tokenStringSingle", "TokenStringSingle"),
  # ("tokenVerbatimStringDouble", "TokenVerbatimStringDouble"),
  # ("tokenVerbatimStringSingle", "TokenVerbatimStringSingle"),

  # ("tokenAssert", "TokenAssert"),
  # ("tokenElse", "TokenElse"),
  # ("tokenError", "TokenError"),
  # ("tokenFalse", "TokenFalse"),
  # ("tokenFor", "TokenFor"),
  # ("tokenFunction", "TokenFunction"),
  # ("tokenIf", "TokenIf"),
  # ("tokenImport", "TokenImport"),
  # ("tokenImportStr", "TokenImportStr"),
  # ("tokenIn", "TokenIn"),
  # ("tokenLocal", "TokenLocal"),
  # ("tokenNullLit", "TokenNullLit"),
  # ("tokenSelf", "TokenSelf"),
  # ("tokenSuper", "TokenSuper"),
  # ("tokenTailStrict", "TokenTailStrict"),
  # ("tokenThen", "TokenThen"),
  # ("tokenTrue", "TokenTrue"),

  # ("tokenEndOfFile", "TokenEndOfFile"),

  # ("token.kind", "Kind"),
  # ("token.fodder", "Fodder"),
  # ("token.data", "Data"),
  # ("token.stringBlockIndent", "StringBlockIndent"),
  # ("token.stringBlockTermIndent", "StringBlockTermIndent"),
  # ("token.loc", "Loc"),
  # ("token", "Token"),

  # ("tokens", "Tokens")

  # ("makeStaticErrorMsg", "MakeStaticErrorMsg"),
  # ("makeStaticErrorPoint", "MakeStaticErrorPoint"),
  # ("makeStaticError", "MakeStaticError"),

  # ("literalField", "LiteralField"),
  # ("identifierSet", "IdentifierSet"),
  # ("NewidentifierSet", "NewIdentifierSet"),
  # ("append", "Append"),

  # ("parse", "Parse"),
]

for k,v in ids:
  call([
    "gorename",
    "-from", '"github.com/google/go-jsonnet".%s' % k,
    "-to", v])