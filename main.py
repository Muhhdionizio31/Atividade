from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Float, Date, Time
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
Base = declarative_base()

class Medico(Base):
    __tablename__ = "medicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    consulta = relationship("Consulta", back_populates= "medicos")

    def __repr__(self):
        return f" Medico: \n - Numero do medico: {self.id} \n Nome: {self.nome} "


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    horario = Column(Time, nullable=False)
    data = Column(Date, nullable=False)
    tipo = Column(String, nullable=False)

    medico_id = Column (Integer, ForeignKey("medicos.id"))

    medico = relationship("Medico", back_populates="consulta")

    def __repr__(self):
        return f"Data: \n {self.data} \n Horario: \n {self.horario} \n - Tipo da consulta: \n {self.tipo}"

engine = create_engine("sqlite:///consultorio.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)