class Config:
    def __init__(self):
        f=open('cfg')
        lines=f.read().splitlines()
        for line in lines:
            if '//' in line or line.strip()=='':
                continue
            
            parse = 'self.'+line
            exec(parse)
