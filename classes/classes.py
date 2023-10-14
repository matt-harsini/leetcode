class Person:
    def __init__(self, name, age) -> None:
       self.name = name 
       self.age = age
       self.todos = []
    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")
    def addTodo(self, todo):
        self.todos.append(todo)
        print("Todo added")
    def showTodos(self):
        for todo in self.todos:
            print(todo)

matthew = Person("Matthew", 23)

matthew.greet()
matthew.addTodo("Go grocery shopping")
matthew.showTodos()