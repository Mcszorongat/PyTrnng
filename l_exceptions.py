# Mechanism for interrupting normal program flow and continuing in sorrounding context
# 1. Raising an exception
# 2. Handling an exception
# 3. Unhandled exception
# 4. Exception object

import la_exceptional as c


print(c.convert1("one two three".split()))
print(c.convert2("asd"))
print(c.convert2(1))
print(c.convert3("asd".split()))
print(c.convert4("asd".split()))
print(c.convert5("asd".split()))

print(c.convert5("nine".split()))
print(c.string_log("nine".split()))

print(c.string_log("ninne".split()))
