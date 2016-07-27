
.PHONY: test


API_VERSION=dev

default: compile


compile:
	kb-sdk install -l js -t ${API_VERSION} GenomeAnnotationAPI
	kb-sdk install -l js -t ${API_VERSION} TaxonAPI
	kb-sdk install -l js -t ${API_VERSION} AssemblyAPI

	kb-sdk install -l python -t ${API_VERSION} GenomeAnnotationAPI
	kb-sdk install -l python -t ${API_VERSION} TaxonAPI
	kb-sdk install -l python -t ${API_VERSION} AssemblyAPI

clean:
	rm -rfv lib/*
	
