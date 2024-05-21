class x:
    def __iter__(self):
        self.n = 1;
        return self;

    def __next__(self):
        if self.n > 10:
            raise StopIteration;
        y = self.n;
        self.n += 1;
        return y;

myclass = x();
iterator = iter(myclass);
print(next(iterator));
print(next(iterator));
print(next(iterator));
