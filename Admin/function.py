def handle_uploaded_file(f):
    with open('media/images'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            print(chunk)
            destination.write(chunk)