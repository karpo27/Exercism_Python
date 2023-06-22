import secrets as sc

def private_key(p):
    global private
    global b
    private = sc.choice(range(2, p))
    b = sc.choice(range(2, p))

    return private

def public_key(p, g, private):
    global public
    public = (g ** private) % p
    
    return public

def secret(p, public, private):
    s_a = (public ** private) % p
    
    return s_a
