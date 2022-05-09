from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    people_favorites = db.relationship('People_favorites', backref="user")
    vehicles_favorites = db.relationship('Vehicles_favorites', backref="user")
    planets_favorites = db.relationship('Planets_favorites', backref="user")

    def get_people(self):
        return list(map(lambda person: person.to_dict(), self.people))
    
    def get_planets(self):
        return list(map(lambda planet: planet.to_dict(), self.planets))
    
    def get_ships(self):
        return list(map(lambda ship: ship.to_dict(), self.ships))


    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'age': self.age
        }

class People(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(255), nullable=False)  
    gender = db.Column(db.String(255))  
    birth_year = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(255)) 
    eye_color : db.Column(db.String(255)) 
    

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def serialize(self):
        return{
            'id': self.id,
            'name': self.username,
            'gender': self.gender,
            'birth_year': self.birth_year,
            'height': self.height,
            'hair_color': self.hair_color,
            'eye_color': self.eye_color

        }

class People_favorites(db.Model):
    __tablename__ = 'people_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'))  
    people_id = db.Column(db.Integer, db.ForeignKey('people.id')) 
    people = db.relationship('People', backref='people_favorite')

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def serialize(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'people_id': self.people_id
        }

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(255), nullable=False) 
    model = db.Column(db.String(255), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    crew_capacity = db.Column(db.Integer, nullable=False)
    vehicle_class  = db.Column(db.String(255), nullable=False) 

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'length': self.length,
            'crew_capacity': self.crew_capacity,
            'vehicle_class': self.vehicle_class
            

        }

class Vehicles_favorites(db.Model):
    __tablename__ =  'vehicle_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'))
    vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicles = db.relationship('Vehicles', backref='vehicles_favorite')

    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def serialize(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'vehicles_id': self.people_id
        }


class Planets(db.Model):
    __tablename__ =  'planets'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(255), nullable=False) 
    climate = db.Column(db.String(255), nullable=False) 
    terrain = db.Column(db.String(255), nullable=False) 
    population  = db.Column(db.Integer, nullable=False)
    gravity  = db.Column(db.Integer, nullable=False)
    orbital_period =  db.Column(db.Integer, nullable=False)


    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  

    def serialize(self):
        return{
            'id': self.id,
            'name': self.username,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population,
            'gravity': self.gravity,
            'orbital_period': self.orbital_period

        }

class Planets_favorites(db.Model):
    __tablename__ = 'planets_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship('Planets', backref='planets_favorite')
    
    def save(self):
        db.session.add(self)  
        db.session.commit()  

    def update(self):
        db.session.commit()  

    def delete(self):
        db.session.delete(self)  
        db.session.commit()  
    
    def serialize(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'planets_id': self.people_id
        }