from ..factory import Type


class inputIdentityDocument(Type):
    #  identity document to be saved to Telegram Passport @number
    #  number; 1-24 characters @expiry_date Document expiry date, if available
    #  Front side of the document

    number = None  # type: "string"
    expiry_date = None  # type: "date"
    front_side = None  # type: "InputFile"
    reverse_side = None  # type: "InputFile"
    selfie = None  # type: "InputFile"
    translation = None  # type: "vector<InputFile>"
