# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from ploneconf.site import _
from ploneconf.site.vocabularies import RegistryValueVocabulary
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema


class ITalk(model.Schema):
    """Dexterity-Schema for Speaker
    """

    directives.widget(type_of_talk=RadioFieldWidget)
    type_of_talk = schema.Choice(
        title=_(u'Type of talk'),
        source=RegistryValueVocabulary('ploneconf.types_of_talk'),
        required=True,
        )

    details = RichText(
        title=u'Details',
        description=_(u'Description of the talk (max. 2000 characters)'),
        max_length=2000,
        required=False,
        )

    directives.widget(audience=CheckBoxFieldWidget)
    audience = schema.Set(
        title=_(u'Audience'),
        description=u'',
        value_type=schema.Choice(
            source=RegistryValueVocabulary('ploneconf.audiences'),
            )
        )

    directives.widget(room=RadioFieldWidget)
    directives.write_permission(room='cmf.ManagePortal')
    room = schema.Choice(
        title=_(u'Room'),
        description=u'',
        source=RegistryValueVocabulary('ploneconf.rooms'),
        required=False,
        )

    speaker = schema.TextLine(
        title=_(u'Speaker'),
        description=_(u'Name (or names) of the speaker'),
        required=False,
        )

    email = Email(
        title=_(u'Email'),
        description=_(u'Email adress of the speaker'),
        required=False,
        )

    image = NamedBlobImage(
        title=_(u'Image'),
        description=u'',
        required=False,
        )

    speaker_biography = RichText(
        title=_(u'Speaker Biography'),
        description=u'',
        max_length=1000,
        required=False,
        )
