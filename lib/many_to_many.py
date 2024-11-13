class Author:
    all = []

    # initialize new Author instance
    def __init__(self, name):
        self.name = name
        # each instance keeps track of its contracts
        self._contracts = []
        # instance adds itself to Class list of instances
        Author.all.append(self)

    def contracts(self):
        return self._contracts
    
    def books(self):
        # returns list of an Authors books via Contract intermediary
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        # verifying that instances are of correct Class structure
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        
        # assigning the data to a new Contract object
        contract = Contract(self, book, date, royalties)

        # append the contract to the instance list of contracts
        self._contracts.append(contract)
        return contract
    
    def total_royalties(self):
        # summing royalties of each contract in referenced Author instance
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):

        # verifying that instances are of correct Class structure
        if not isinstance(author, Author):
            raise ValueError("Author must be Author Object.")
        if not isinstance(book, Book):
            raise ValueError("Book must be Book Object.")
        if not isinstance(date, str):
            raise ValueError("Date must be a string.")
        if not isinstance(royalties, int):
            raise ValueError("Royalties must be an integer.")
        
        # assign instance attributes
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # add contract to author's list of contracts
        self.author._contracts.append(self)

        # add contract to book's list of contracts
        self.book._contracts.append(self)
        # append contract instance to Contract class list of contracts
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]