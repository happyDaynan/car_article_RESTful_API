from server import db

class articleModels(db.Model):
    __tablename__ = 'brand_href'
    article_id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(4))
    brand = db.Column(db.String(4))
    href = db.Column(db.String(40))
    todbtime = db.Column(db.DateTime)
    articletype = db.Column(db.Boolean)

    def __init__(self, article_id, country, brand, href, todbtime, articletype= 0):
        self.article_id = article_id
        self.country = country
        self.brand = brand
        self. href = href
        self.todbtime = todbtime
        self.articletype = articletype
    
    def serizlize(self):
        return {
            "article_id" : self.article_id,
            "country" : self.country,
            "brand" : self.brand,
            "href" : self.href,
            "todbtime": self.todbtime,
            "articletype": self.articletype,
        }

"""
這邊設定完成後，要去user.py做引入
"""