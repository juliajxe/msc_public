import Person

ds = Person.DistanceStudent(
    Person.Name("Mr", "John", "Greenhold", ["Stuart"]),
    currentModule="Advanced Programming"
)

print(ds.isStudying())
