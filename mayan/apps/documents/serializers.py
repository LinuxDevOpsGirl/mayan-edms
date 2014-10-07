from __future__ import absolute_import

from rest_framework import serializers

from .models import Document, DocumentVersion, DocumentPage, DocumentType


class DocumentPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentPage


class DocumentVersionSerializer(serializers.HyperlinkedModelSerializer):
    pages = DocumentPageSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = DocumentVersion
        read_only_fields = ('document',)


class DocumentImageSerializer(serializers.Serializer):
    status = serializers.CharField()
    data = serializers.CharField()


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    versions = DocumentVersionSerializer(many=True, read_only=True)
    image = serializers.HyperlinkedIdentityField(view_name='document-image')
    new_version = serializers.HyperlinkedIdentityField(view_name='document-new-version')

    class Meta:
        fields = ('id', 'url', 'image', 'new_version', 'uuid', 'document_type', 'description', 'date_added', 'versions')
        model = Document


class DocumentTypeSerializer(serializers.HyperlinkedModelSerializer):
    documents = serializers.HyperlinkedIdentityField(view_name='documenttype-document-list')

    class Meta:
        model = DocumentType
        fields = ('id', 'url', 'name', 'documents')
