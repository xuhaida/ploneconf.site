# -*- coding: utf-8 -*-
from inspect import currentframe
from plone import api
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def RegistryValueVocabularyFactory(context):
    # get the name of this utility by inspecting the previous stack
    name = currentframe().f_back.f_locals.get('name', None)
    if name is None:
        name = currentframe().f_back.f_locals.get('vocabulary', None)
    if name is None:
        return []
    name = str(name)
    values = api.portal.get_registry_record(name)
    return safe_simplevocabulary_from_values(values)
