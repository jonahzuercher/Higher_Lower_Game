class fill:
    def Spaces(word, totalChars):
        output = ""
        if len(str(word)) < int(totalChars):
            buchstaben = list(str(word))
            while len(buchstaben) <= int(totalChars):
                buchstaben.insert(0, " ")
                if len(buchstaben) == int(totalChars):
                    break
                elif len(buchstaben) != int(totalChars)-1:
                    buchstaben.insert(len(buchstaben), " ")
            for i in buchstaben:
                output += i
            return output
        elif len(str(word)) >= int(totalChars):
            return word
