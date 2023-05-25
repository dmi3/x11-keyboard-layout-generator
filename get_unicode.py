character = "⚠"
temp_unicode = hex(ord(character))
unicode = "U" + temp_unicode.upper()[2:]
print(unicode)
