"""
MacFinder - simple Macbook lookup class
"""

class Macbook:
    def __init__(self, name, exp, model, response, money_av, cond):
        """
        name: str - user name
        exp: int (0-5) - experience rating
        model: str - model to lookup for specs
        response: str - model to lookup for ideal uses (can be same as model)
        money_av: numeric - available money (unused by this simple example)
        cond: "NEW" or "REF" - shows new or refurbished price lists
        """
        self.name = name
        self.exp = exp
        self.model = model
        self.response = response
        self.money_av = money_av
        self.cond = cond

        self.responses = {
            0: "We are going to try and change that rating!",
            1: "Well, there is definitely room for improvement!",
            2: "We are confident this number can become much higher!",
            3: "We believe we can make it a five!",
            4: "Brace yourselves! A new champion is emerging.",
            5: "You're already a master, but let's go even further!"
        }

        self.mac_specs = {
            "Apple MacBook Pro (2020)": "Release date: 2020 | Chip: M1 | Display: 13.3\"",
            "Apple MacBook Air (2020)": "Release date: 2020 | Chip: M1 | Display: 13\"",
            "Apple MacBook Air (2022)": "Release date: 2022 | Chip: M2 | Display: 13.6\"",
            "Apple MacBook Pro (2022)": "Release date: 2022 | Chip: M2 | Display: 13.3\"",
            "Apple MacBook Air (2023)": "Release date: 2023 | Chip: M2 | Display: 15.3\"",
            "Apple MacBook Air (2024)": "Release date: 2024 | Chip: M3 | Display: 13.6 / 15.3\"",
            "Apple MacBook Pro (2023)": "Release date: 2023 | Chip: M3 family | Display: 14.2 / 16.2\"",
            "Apple MacBook Air (2025)": "Release date: 2025 | Chip: M4 | Display: 13.6\"",
            "Apple MacBook Air (2025) Advanced": "Release date: 2025 | Chip: M4 | Display: 15.3\"",
            "Apple MacBook Pro (2024)": "Release date: 2024 | Chip: M4 Pro/Max | Display: 14.2 / 16.2\"",
            "Apple MacBook Pro (2025)": "Release date: 2025 | Chip: M5 | Display: 14.2\""
        }

        self.mac_ideal = {
            "Apple MacBook Pro (2020)": "Students, programmers, everyday users, light creative work.",
            "Apple MacBook Air (2020)": "Portability + full Mac performance on a budget.",
            "Apple MacBook Air (2022)": "Students, office, light photo/video work.",
            "Apple MacBook Pro (2022)": "Programmers, sustained workloads.",
            "Apple MacBook Air (2023)": "Users who want a larger display.",
            "Apple MacBook Air (2024)": "Best efficiency machine.",
            "Apple MacBook Pro (2023)": "Heavy workloads and creative tasks.",
            "Apple MacBook Air (2025)": "Everyday users who want M4 efficiency.",
            "Apple MacBook Air (2025) Advanced": "Light creators, big screen.",
            "Apple MacBook Pro (2024)": "Video editing, 3D, AI.",
            "Apple MacBook Pro (2025)": "Fastest MacBook available."
        }

        self.mac_new_price = {
            "Apple MacBook Pro (2020)": "Brand new: $1499–1899",
            "Apple MacBook Air (2020)": "Brand new: $899–999",
            "Apple MacBook Air (2022)": "Brand new: $1099–1399",
            "Apple MacBook Pro (2022)": "Brand new: $1199–1499",
            "Apple MacBook Air (2023)": "Brand new: $1299–1649",
            "Apple MacBook Air (2024)": "Brand new: $1099–1499",
            "Apple MacBook Pro (2023)": "Brand new: $1599–2499",
            "Apple MacBook Air (2025)": "Brand new: $899–1049",
            "Apple MacBook Air (2025) Advanced": "Brand new: $999–1199",
            "Apple MacBook Pro (2024)": "Brand new: $2199–4399",
            "Apple MacBook Pro (2025)": "Brand new: $1799–2299"
        }

        self.mac_ref_price = {
            "Apple MacBook Pro (2020)": "Refurbished: $590–790",
            "Apple MacBook Air (2020)": "Refurbished: $420–700",
            "Apple MacBook Air (2022)": "Refurbished: $700–900",
            "Apple MacBook Pro (2022)": "Refurbished: $800–1100",
            "Apple MacBook Air (2023)": "Refurbished: $1000–1300",
            "Apple MacBook Air (2024)": "Refurbished: $800–1200",
            "Apple MacBook Pro (2023)": "Refurbished: $1300–2000",
            "Apple MacBook Air (2025)": "Refurbished: $650–800",
            "Apple MacBook Air (2025) Advanced": "Refurbished: $850–1000",
            "Apple MacBook Pro (2024)": "Refurbished: $1800–3500",
            "Apple MacBook Pro (2025)": "Refurbished: $1600–2000"
        }

    def intro(self):
        print(f"Welcome to MacFinder, {self.name}! Here you can submit any MacBook model from 2020 and onwards, and I'll show you its specs.\n")
        if not isinstance(self.exp, int) or not (0 <= self.exp <= 5):
            print("Submit a valid whole number from 0–5.")
            return
        print(self.responses.get(self.exp, "Thanks for your input!"))

    def mac(self):
        """Print specs for the model in self.model"""
        specs = self.mac_specs.get(self.model)
        if specs:
            print(f"Specs for {self.model}: {specs}")
        else:
            print("Please enter a valid MacBook model from the mac list.")

    def mac_extended(self):
        """Print ideal user categories for the model in self.response"""
        ideal = self.mac_ideal.get(self.response)
        if ideal:
            print(f"Ideal use cases for {self.response}: {ideal}")
        else:
            print("Invalid model for extended info.")

    def mac_cash(self):
        """Print price lists depending on condition NEW or REF"""
        cond = (self.cond or "").upper()
        if cond == "NEW":
            for model, price in self.mac_new_price.items():
                print(f"{model}: {price}")
        elif cond == "REF":
            for model, price in self.mac_ref_price.items():
                print(f"{model}: {price}")
        else:
            print("Invalid condition. Use NEW or REF.")