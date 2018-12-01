# -*- coding: utf-8 -*-
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IContextSourceBinder


@implementer(IVocabularyFactory)
class RoomsVocabularyFactory(object):

    def __call__(self, context):
        values = api.portal.get_registry_record('ploneconf.rooms')
        normalizer = queryUtility(IIDNormalizer)
        items = [(normalizer.normalize(i), i) for i in values]
        return SimpleVocabulary.fromItems(items)

RoomsVocabulary = RoomsVocabularyFactory()

@implementer(IContextSourceBinder)
class RegistryValueVocabulary(object):

    def __init__(self, value_name):
        self.value_name = value_name

    def __call__(self, context):
        values = api.portal.get_registry_record(self.value_name)
        return safe_simplevocabulary_from_values(values)
