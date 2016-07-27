# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class TaxonAPI(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver='dev'):
        if url is None:
            url = 'https://kbase.us/services/service_wizard'
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            lookup_url=True)

    def get_parent(self, ref, context=None):
        """
        Retrieve parent Taxon.
        @return Reference to parent Taxon.
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectReference"
        """
        return self._client.call_method(
            'TaxonAPI.get_parent',
            [ref], self._service_ver, context)

    def get_children(self, ref, context=None):
        """
        Retrieve children Taxon.
        @return List of references to child Taxons.
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of type "ObjectReference"
        """
        return self._client.call_method(
            'TaxonAPI.get_children',
            [ref], self._service_ver, context)

    def get_genome_annotations(self, ref, context=None):
        """
        funcdef GenomeAnnotation(s) that refer to this Taxon.
         If this is accessing a KBaseGenomes.Genome object, it will
         return an empty list (this information is not available).
         @return List of references to GenomeAnnotation objects.
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of type "ObjectReference"
        """
        return self._client.call_method(
            'TaxonAPI.get_genome_annotations',
            [ref], self._service_ver, context)

    def get_scientific_lineage(self, ref, context=None):
        """
        Retrieve the scientific lineage.
        @return Strings for each 'unit' of the lineage, ordered in
          the usual way from Domain to Kingdom to Phylum, etc.
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of String
        """
        return self._client.call_method(
            'TaxonAPI.get_scientific_lineage',
            [ref], self._service_ver, context)

    def get_scientific_name(self, ref, context=None):
        """
        Retrieve the scientific name.
        @return The scientific name, e.g., "Escherichia Coli K12 str. MG1655"
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
        return self._client.call_method(
            'TaxonAPI.get_scientific_name',
            [ref], self._service_ver, context)

    def get_taxonomic_id(self, ref, context=None):
        """
        Retrieve the NCBI taxonomic ID of this Taxon.
        For type KBaseGenomes.Genome, the ``source_id`` will be returned.
        @return Integer taxonomic ID.
        :param ref: instance of type "ObjectReference"
        :returns: instance of Long
        """
        return self._client.call_method(
            'TaxonAPI.get_taxonomic_id',
            [ref], self._service_ver, context)

    def get_kingdom(self, ref, context=None):
        """
        Retrieve the kingdom.
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
        return self._client.call_method(
            'TaxonAPI.get_kingdom',
            [ref], self._service_ver, context)

    def get_domain(self, ref, context=None):
        """
        Retrieve the domain.
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
        return self._client.call_method(
            'TaxonAPI.get_domain',
            [ref], self._service_ver, context)

    def get_genetic_code(self, ref, context=None):
        """
        Retrieve the genetic code.
        :param ref: instance of type "ObjectReference"
        :returns: instance of Long
        """
        return self._client.call_method(
            'TaxonAPI.get_genetic_code',
            [ref], self._service_ver, context)

    def get_aliases(self, ref, context=None):
        """
        Retrieve the aliases.
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of String
        """
        return self._client.call_method(
            'TaxonAPI.get_aliases',
            [ref], self._service_ver, context)

    def get_info(self, ref, context=None):
        """
        Retrieve object info.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectInfo" (* @skip documentation) ->
           structure: parameter "object_id" of Long, parameter "object_name"
           of String, parameter "object_reference" of String, parameter
           "object_reference_versioned" of String, parameter "type_string" of
           String, parameter "save_date" of String, parameter "version" of
           Long, parameter "saved_by" of String, parameter "workspace_id" of
           Long, parameter "workspace_name" of String, parameter
           "object_checksum" of String, parameter "object_size" of Long,
           parameter "object_metadata" of mapping from String to String
        """
        return self._client.call_method(
            'TaxonAPI.get_info',
            [ref], self._service_ver, context)

    def get_history(self, ref, context=None):
        """
        Retrieve object history.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectHistory" (* @skip documentation) ->
           list of type "ObjectInfo" (* @skip documentation) -> structure:
           parameter "object_id" of Long, parameter "object_name" of String,
           parameter "object_reference" of String, parameter
           "object_reference_versioned" of String, parameter "type_string" of
           String, parameter "save_date" of String, parameter "version" of
           Long, parameter "saved_by" of String, parameter "workspace_id" of
           Long, parameter "workspace_name" of String, parameter
           "object_checksum" of String, parameter "object_size" of Long,
           parameter "object_metadata" of mapping from String to String
        """
        return self._client.call_method(
            'TaxonAPI.get_history',
            [ref], self._service_ver, context)

    def get_provenance(self, ref, context=None):
        """
        Retrieve object provenance.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectProvenance" (* @skip documentation)
           -> list of type "ObjectProvenanceAction" (* @skip documentation)
           -> structure: parameter "time" of String, parameter "service_name"
           of String, parameter "service_version" of String, parameter
           "service_method" of String, parameter "method_parameters" of list
           of String, parameter "script_name" of String, parameter
           "script_version" of String, parameter "script_command_line" of
           String, parameter "input_object_references" of list of String,
           parameter "validated_object_references" of list of String,
           parameter "intermediate_input_ids" of list of String, parameter
           "intermediate_output_ids" of list of String, parameter
           "external_data" of list of type "ExternalDataUnit" (* @skip
           documentation) -> structure: parameter "resource_name" of String,
           parameter "resource_url" of String, parameter "resource_version"
           of String, parameter "resource_release_date" of String, parameter
           "data_url" of String, parameter "data_id" of String, parameter
           "description" of String, parameter "description" of String
        """
        return self._client.call_method(
            'TaxonAPI.get_provenance',
            [ref], self._service_ver, context)

    def get_id(self, ref, context=None):
        """
        Retrieve object identifier.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of Long
        """
        return self._client.call_method(
            'TaxonAPI.get_id',
            [ref], self._service_ver, context)

    def get_name(self, ref, context=None):
        """
        Retrieve object name.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
        return self._client.call_method(
            'TaxonAPI.get_name',
            [ref], self._service_ver, context)

    def get_version(self, ref, context=None):
        """
        Retrieve object version.
        @skip documentation
        :param ref: instance of type "ObjectReference"
        :returns: instance of String
        """
        return self._client.call_method(
            'TaxonAPI.get_version',
            [ref], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('TaxonAPI.status',
            [], self._service_ver, context)
