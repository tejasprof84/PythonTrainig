class UserRegistration:

    @staticmethod
    def validate_email(mail):        #static methhod where no object instance created using self or cls
                                        #and no class attribute is accessed or used 
        # 1. Check minimum length
        if len(mail) < 8:
            print("Email too short")
            return False
        
        # 2. Email must contain exactly one '@'
        if mail.count("@") != 1:
            print("Email must contain exactly one '@'")
            return False
        
        # 3. Check uppercase and lowercase requirement
        has_upper = any(ch.isupper() for ch in mail)
        has_lower = any(ch.islower() for ch in mail)  ##any checks for each element if one ele is satisfied condition then 
                                                       #it will return true
        has_digit = any(ch.isdigit() for ch in mail)

        if not has_upper:
            print("Email must contain at least one uppercase letter")
            return False
        
        if not has_lower:
            print("Email must contain at least one lowercase letter")
            return False

        if not has_digit:
            print("Email must contain at least one Numerical digit")
            return False
        
        # 4. Split into username and domain
        username,domain =  mail.split("@")
        ##print(username)
        ##print(domain)
        
        
        # 5. Both sides must be non-empty and domain must be 'gmail.com'
        if not username or domain != "gmail.com":   ##---> checks for username is not empty and domain is "gmail.com"--> not True or False=False
                                                                                                #Donn123 @ gmail.com (do't go inside if condition)
            print("Email format invalid: missing username or domain is not gmail.com")
            return False
        
        print("Valid email format")
        return True


result = UserRegistration.validate_email(str(input("Enter your Mail ")))
print("Validation result:", result)



"""
class UserRegistration:

    @staticmethod
    def validate_email(mail):
        if len(mail) > 8:
            for i in mail:       
                if i == "@":
                    #print("validate email successful")
                    return 
            else:
                print("Invalid email format")
                return False
        
            

result = UserRegistration.validate_email("jbjejask")
print("Validation result:", result)
"""