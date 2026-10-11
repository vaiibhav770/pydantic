class RuleModel:
    def predict(self, df):
        out = []
        for _, r in df.iterrows():
            score = {'young': 0, 'middle-aged': 1, 'old': 2}[r['age_group']]
            score += {'low': 0, 'medium': 1, 'high': 2}[r['lifeStypeRisk']]
            score += 1 if r['bmi'] > 30 else 0
            score += 1 if r['occupation'] in ('army', 'police') else 0
            score += 1 if r['city_tire'] == 'tire1' else 0
            score += 1 if r['income_lpa'] < 8 else 0
            if score <= 2:
                out.append('Low')
            elif score <= 4:
                out.append('Medium')
            else:
                out.append('High')
        return out