
.PHONY: test

default: compile


compile:
	kb-sdk install -l js GenomeAnnotationAPI
	kb-sdk install -l js TaxonAPI
	kb-sdk install -l js AssemblyAPI

clean:
	rm -rfv lib/*
	
