class Config:
    def __init__(self):
        f=open('cfg')
        lines=f.read().splitlines()
        for line in lines:
            if 'NCYCLE=' in line:
                self.ncycle=int(line.replace('NCYCLE=',''))
            elif 'BATCH_SIZE=' in line:
                self.batch_size=int(line.replace('BATCH_SIZE=',''))
            elif 'EPOCHS=' in line:
                self.epochs=int(line.replace('EPOCHS=',''))
            elif 'GAMMA_TD=' in line:
                self.gamma_td=float(line.replace('GAMMA_TD=',''))
            elif 'EPS_TD=' in line:
                self.eps_td=float(line.replace('EPS_TD=',''))
            elif 'EPS_PRED=' in line:
                self.eps_pred=float(line.replace('EPS_PRED=',''))
            elif 'USE_SAMPLE_WEIGHT=' in line:
                if line.replace('USE_SAMPLE_WEIGHT=','')=='True':
                    self.use_sample_weight=True
                else:
                    self.use_sample_weight=False
            elif 'AIGAMES=' in line:
                self.aiGames=int(line.replace('AIGAMES=',''))
            elif 'GAMEMODE=' in line:
                self.mode=line.replace('GAMEMODE=','')
            elif 'EPS_DECAY_RATE=' in line:
                self.eps_decay_rate=float(line.replace('EPS_DECAY_RATE=',''))             
