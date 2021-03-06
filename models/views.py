# -*- coding:utf-8 -*-

##############################################################################
# MobilEPR - A small self-hosted ERP that works with your smartphone.
# Copyright (C) 2017  Eligio Becerra
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

"""
views.py in models

This package doesn't provide any views to the api Blueprint, instead it
handles all of the views in the database, intead of creating them as a
separate entity inside this model.
"""


from sqlalchemy import Column, Integer, DateTime, PrimaryKeyConstraint,\
                       String, Float
from models import Base

from datetime import datetime


class SalesReport(Base):

    __tablename__ = "SalesView"

    __table_args__ = (
        PrimaryKeyConstraint('idSale', 'name'),
    )

    idSale = Column(Integer)
    date = Column(DateTime)
    name = Column(String(700))
    productPrice = Column(Float(precision=2))
    units = Column(Integer)
    total_earning = Column(Float(precision=2))

    initDate = ""
    endDate = ""

    def __init__(self, initDate="", endDate=""):
        if not initDate == "" and not endDate == "":
            self.initDate = initDate
            self.endDate = endDate

    @property
    def serialize(self):
        return {'idSale': self.idSale, 'date': self.date,
                'nameme': self.name, 'productPrice': self.productPrice,
                'units': self.units, 'total_earning': self.total_earning}

class DepletedItems(Base):

    __tablename__ = "DepletedItemsView"

    __table_args__ = (
        PrimaryKeyConstraint('idSale', 'barcode', 'date'),
    )

    idSale = Column(Integer)
    date = Column(DateTime)
    name = Column(String(700))
    barcode = Column(String(50))

    @property
    def serialize(self):
        return {'idSale': self.idSale, 'date': self.date,
                'name': self.name, 'productPrice': self.barcode}