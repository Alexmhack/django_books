with open('books.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        count += 1
        if count == 1:
            continue
        obj, created = Book.objects.get_or_create(
            isbn=row[0],
            title=row[1],
            author=row[2],
            year=int(row[3])
        )
        string = ""
        if obj:
            string = "EXISTS"
        if created:
            string = "CREATED"
        print(f"Object {string}: {count}")
    print("TOTAL OBJECTS: {count}")
