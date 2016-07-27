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


class GenomeAnnotationAPI(object):

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

    def get_taxon(self, ref, context=None):
        """
        Retrieve the Taxon associated with this GenomeAnnotation.
        @return Reference to TaxonAPI object
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectReference"
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_taxon',
            [ref], self._service_ver, context)

    def get_assembly(self, ref, context=None):
        """
        Retrieve the Assembly associated with this GenomeAnnotation.
        @return Reference to AssemblyAPI object
        :param ref: instance of type "ObjectReference"
        :returns: instance of type "ObjectReference"
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_assembly',
            [ref], self._service_ver, context)

    def get_feature_types(self, ref, context=None):
        """
        Retrieve the list of Feature types.
        @return List of feature type identifiers (strings)
        :param ref: instance of type "ObjectReference"
        :returns: instance of list of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_types',
            [ref], self._service_ver, context)

    def get_feature_type_descriptions(self, ref, feature_type_list, context=None):
        """
        Retrieve the descriptions for each Feature type in
        this GenomeAnnotation.
        @param feature_type_list List of Feature types. If this list
         is empty or None,
         the whole mapping will be returned.
        @return Name and description for each requested Feature Type
        :param ref: instance of type "ObjectReference"
        :param feature_type_list: instance of list of String
        :returns: instance of mapping from String to String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_type_descriptions',
            [ref, feature_type_list], self._service_ver, context)

    def get_feature_type_counts(self, ref, feature_type_list, context=None):
        """
        Retrieve the count of each Feature type.
        @param feature_type_list  List of Feature Types. If empty,
          this will retrieve  counts for all Feature Types.
        :param ref: instance of type "ObjectReference"
        :param feature_type_list: instance of list of String
        :returns: instance of mapping from String to Long
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_type_counts',
            [ref, feature_type_list], self._service_ver, context)

    def get_feature_ids(self, ref, filters, group_type, context=None):
        """
        Retrieve Feature IDs, optionally filtered by type, region, function, alias.
        @param filters Dictionary of filters that can be applied to contents.
          If this is empty or missing, all Feature IDs will be returned.
        @param group_type How to group results, which is a single string matching one
          of the values for the ``filters`` parameter.
        @return Grouped mapping of features.
        :param ref: instance of type "ObjectReference"
        :param filters: instance of type "Feature_id_filters" (* * Filters
           passed to :meth:`get_feature_ids`) -> structure: parameter
           "type_list" of list of String, parameter "region_list" of list of
           type "Region" -> structure: parameter "contig_id" of String,
           parameter "strand" of String, parameter "start" of Long, parameter
           "length" of Long, parameter "function_list" of list of String,
           parameter "alias_list" of list of String
        :param group_type: instance of String
        :returns: instance of type "Feature_id_mapping" -> structure:
           parameter "by_type" of mapping from String to list of String,
           parameter "by_region" of mapping from String to mapping from
           String to mapping from String to list of String, parameter
           "by_function" of mapping from String to list of String, parameter
           "by_alias" of mapping from String to list of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_ids',
            [ref, filters, group_type], self._service_ver, context)

    def get_features(self, ref, feature_id_list, context=None):
        """
        Retrieve Feature data.
        @param feature_id_list List of Features to retrieve.
          If None, returns all Feature data.
        @return Mapping from Feature IDs to dicts of available data.
        :param ref: instance of type "ObjectReference"
        :param feature_id_list: instance of list of String
        :returns: instance of mapping from String to type "Feature_data" ->
           structure: parameter "feature_id" of String, parameter
           "feature_type" of String, parameter "feature_function" of String,
           parameter "feature_aliases" of mapping from String to list of
           String, parameter "feature_dna_sequence_length" of Long, parameter
           "feature_dna_sequence" of String, parameter "feature_md5" of
           String, parameter "feature_locations" of list of type "Region" ->
           structure: parameter "contig_id" of String, parameter "strand" of
           String, parameter "start" of Long, parameter "length" of Long,
           parameter "feature_publications" of list of String, parameter
           "feature_quality_warnings" of list of String, parameter
           "feature_quality_score" of list of String, parameter
           "feature_notes" of String, parameter "feature_inference" of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_features',
            [ref, feature_id_list], self._service_ver, context)

    def get_proteins(self, ref, context=None):
        """
        Retrieve Protein data.
        @return Mapping from protein ID to data about the protein.
        :param ref: instance of type "ObjectReference"
        :returns: instance of mapping from String to type "Protein_data" ->
           structure: parameter "protein_id" of String, parameter
           "protein_amino_acid_sequence" of String, parameter
           "protein_function" of String, parameter "protein_aliases" of list
           of String, parameter "protein_md5" of String, parameter
           "protein_domain_locations" of list of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_proteins',
            [ref], self._service_ver, context)

    def get_feature_locations(self, ref, feature_id_list, context=None):
        """
        Retrieve Feature locations.
        @param feature_id_list List of Feature IDs for which to retrieve locations.
            If empty, returns data for all features.
        @return Mapping from Feature IDs to location information for each.
        :param ref: instance of type "ObjectReference"
        :param feature_id_list: instance of list of String
        :returns: instance of mapping from String to list of type "Region" ->
           structure: parameter "contig_id" of String, parameter "strand" of
           String, parameter "start" of Long, parameter "length" of Long
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_locations',
            [ref, feature_id_list], self._service_ver, context)

    def get_feature_publications(self, ref, feature_id_list, context=None):
        """
        Retrieve Feature publications.
        @param feature_id_list List of Feature IDs for which to retrieve publications.
            If empty, returns data for all features.
        @return Mapping from Feature IDs to publication info for each.
        :param ref: instance of type "ObjectReference"
        :param feature_id_list: instance of list of String
        :returns: instance of mapping from String to list of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_publications',
            [ref, feature_id_list], self._service_ver, context)

    def get_feature_dna(self, ref, feature_id_list, context=None):
        """
        Retrieve Feature DNA sequences.
        @param feature_id_list List of Feature IDs for which to retrieve sequences.
            If empty, returns data for all features.
        @return Mapping of Feature IDs to their DNA sequence.
        :param ref: instance of type "ObjectReference"
        :param feature_id_list: instance of list of String
        :returns: instance of mapping from String to String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_dna',
            [ref, feature_id_list], self._service_ver, context)

    def get_feature_functions(self, ref, feature_id_list, context=None):
        """
        Retrieve Feature functions.
        @param feature_id_list List of Feature IDs for which to retrieve functions.
            If empty, returns data for all features.
        @return Mapping of Feature IDs to their functions.
        :param ref: instance of type "ObjectReference"
        :param feature_id_list: instance of list of String
        :returns: instance of mapping from String to String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_functions',
            [ref, feature_id_list], self._service_ver, context)

    def get_feature_aliases(self, ref, feature_id_list, context=None):
        """
        Retrieve Feature aliases.
        @param feature_id_list List of Feature IDS for which to retrieve aliases.
            If empty, returns data for all features.
        @return Mapping of Feature IDs to a list of aliases.
        :param ref: instance of type "ObjectReference"
        :param feature_id_list: instance of list of String
        :returns: instance of mapping from String to list of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_feature_aliases',
            [ref, feature_id_list], self._service_ver, context)

    def get_cds_by_gene(self, ref, gene_id_list, context=None):
        """
        Retrieves coding sequence Features (cds) for given gene Feature IDs.
        @param feature_id_list List of gene Feature IDS for which to retrieve CDS.
            If empty, returns data for all features.
        @return Mapping of gene Feature IDs to a list of CDS Feature IDs.
        :param ref: instance of type "ObjectReference"
        :param gene_id_list: instance of list of String
        :returns: instance of mapping from String to list of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_cds_by_gene',
            [ref, gene_id_list], self._service_ver, context)

    def get_cds_by_mrna(self, ref, mrna_id_list, context=None):
        """
        Retrieves coding sequence (cds) Feature IDs for given mRNA Feature IDs.
        @param feature_id_list List of mRNA Feature IDS for which to retrieve CDS.
            If empty, returns data for all features.
        @return Mapping of mRNA Feature IDs to a list of CDS Feature IDs.
        :param ref: instance of type "ObjectReference"
        :param mrna_id_list: instance of list of String
        :returns: instance of mapping from String to String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_cds_by_mrna',
            [ref, mrna_id_list], self._service_ver, context)

    def get_gene_by_cds(self, ref, cds_id_list, context=None):
        """
        Retrieves gene Feature IDs for given coding sequence (cds) Feature IDs.
        @param feature_id_list List of cds Feature IDS for which to retrieve gene IDs.
            If empty, returns all cds/gene mappings.
        @return Mapping of cds Feature IDs to gene Feature IDs.
        :param ref: instance of type "ObjectReference"
        :param cds_id_list: instance of list of String
        :returns: instance of mapping from String to String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_gene_by_cds',
            [ref, cds_id_list], self._service_ver, context)

    def get_gene_by_mrna(self, ref, mrna_id_list, context=None):
        """
        Retrieves gene Feature IDs for given mRNA Feature IDs.
        @param feature_id_list List of mRNA Feature IDS for which to retrieve gene IDs.
            If empty, returns all mRNA/gene mappings.
        @return Mapping of mRNA Feature IDs to gene Feature IDs.
        :param ref: instance of type "ObjectReference"
        :param mrna_id_list: instance of list of String
        :returns: instance of mapping from String to String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_gene_by_mrna',
            [ref, mrna_id_list], self._service_ver, context)

    def get_mrna_by_cds(self, ref, cds_id_list, context=None):
        """
        Retrieves mRNA Features for given coding sequences (cds) Feature IDs.
        @param feature_id_list List of cds Feature IDS for which to retrieve mRNA IDs.
            If empty, returns all cds/mRNA mappings.
        @return Mapping of cds Feature IDs to mRNA Feature IDs.
        :param ref: instance of type "ObjectReference"
        :param cds_id_list: instance of list of String
        :returns: instance of mapping from String to String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_mrna_by_cds',
            [ref, cds_id_list], self._service_ver, context)

    def get_mrna_by_gene(self, ref, gene_id_list, context=None):
        """
        Retrieve the mRNA IDs for given gene IDs.
        @param feature_id_list List of gene Feature IDS for which to retrieve mRNA IDs.
            If empty, returns all gene/mRNA mappings.
        @return Mapping of gene Feature IDs to a list of mRNA Feature IDs.
        :param ref: instance of type "ObjectReference"
        :param gene_id_list: instance of list of String
        :returns: instance of mapping from String to list of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_mrna_by_gene',
            [ref, gene_id_list], self._service_ver, context)

    def get_mrna_exons(self, ref, mrna_id_list, context=None):
        """
        Retrieve Exon information for each mRNA ID.
        @param feature_id_list List of mRNA Feature IDS for which to retrieve exons.
            If empty, returns data for all exons.
        @return Mapping of mRNA Feature IDs to a list of exons (:js:data:`Exon_data`).
        :param ref: instance of type "ObjectReference"
        :param mrna_id_list: instance of list of String
        :returns: instance of mapping from String to list of type "Exon_data"
           -> structure: parameter "exon_location" of type "Region" ->
           structure: parameter "contig_id" of String, parameter "strand" of
           String, parameter "start" of Long, parameter "length" of Long,
           parameter "exon_dna_sequence" of String, parameter "exon_ordinal"
           of Long
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_mrna_exons',
            [ref, mrna_id_list], self._service_ver, context)

    def get_mrna_utrs(self, ref, mrna_id_list, context=None):
        """
        Retrieve UTR information for each mRNA Feature ID.
         UTRs are calculated between mRNA features and corresponding CDS features.
         The return value for each mRNA can contain either:
            - no UTRs found (empty dict)
            -  5' UTR only
            -  3' UTR only
            -  5' and 3' UTRs
         Note: The Genome data type does not contain interfeature
         relationship information. Calling this method for Genome objects
         will raise a :js:throws:`exc.TypeException`.
        @param feature_id_list List of mRNA Feature IDS for which to retrieve UTRs.
        If empty, returns data for all UTRs.
        @return Mapping of mRNA Feature IDs to a mapping that contains
        both 5' and 3' UTRs::
            { "5'UTR": :js:data:`UTR_data`, "3'UTR": :js:data:`UTR_data` }
        :param ref: instance of type "ObjectReference"
        :param mrna_id_list: instance of list of String
        :returns: instance of mapping from String to mapping from String to
           type "UTR_data" -> structure: parameter "utr_locations" of list of
           type "Region" -> structure: parameter "contig_id" of String,
           parameter "strand" of String, parameter "start" of Long, parameter
           "length" of Long, parameter "utr_dna_sequence" of String
        """
        return self._client.call_method(
            'GenomeAnnotationAPI.get_mrna_utrs',
            [ref, mrna_id_list], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('GenomeAnnotationAPI.status',
            [], self._service_ver, context)