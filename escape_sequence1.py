#output: line A \n line b
print("Line A \\n Line b")
print("Line A \\t line b")
#output: \" \' 
print("\\\" \\\' ")
#output: \' - '(b)
print("\\\' - \'(b)")
#output: \\ - \ (a)
print("\\\\ - \\ (a)")
#output: \\\' - \'
print("\\\\\\\' - \\\'")