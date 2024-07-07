def main():
    message = input("File name: ").lower().strip()
    print(extensions(message))



def extensions(text):
    parts = text.split(".")

# check if parts contains atleast 2 strings
    if len(parts) < 2:
        return "application/octet-stream"

# we use the last string everytime
    part2 = parts[-1]

    if part2 == "gif" or part2 == "jpeg" or part2 == "png":
        return "image/" + part2
    elif part2 == "jpg":
        return "image/jpeg"
    elif part2 == "pdf" or part2 == "zip":
        return "application/" + part2
    elif part2 == "txt":
        return "text/plain"
    else:
        return "application/octet-stream"


main()
