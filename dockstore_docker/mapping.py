def custom_mapping(cls):
    mapping = {
        "@context": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "@id": {"type": "keyword"},
        "@type": {"type": "keyword", "copy_to": ["all"]},
        "abstract": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
        "all": {
            "type": "text",
            "analyzer": "nde_analyzer",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "aggregateRating": {
            "properties": {
                "@type": {"type": "text"},
                "ratingCount": {"type": "unsigned_long"},
                "ratingValue": {"type": "double"},
                "reviewAspect": {"type": "text"}
            }
        },
        "alternateName": {"type": "text", "copy_to": ["all"]},
        "applicationCategory": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
        "applicationSubCategory": {"type": "keyword", "copy_to": ["all"]},
        "applicationSuite": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
        "author": {
            "properties": {
                "@type": {"type": "text"},
                "affiliation": {
                    "properties": {
                        "@type": {"type": "keyword", "copy_to": ["all"]},
                        "name": {"type": "keyword", "copy_to": ["all"]},
                        "sameAs": {"type": "keyword", "copy_to": ["all"]},
                    }
                },
                "familyName": {"type": "text", "copy_to": ["all"]},
                "givenName": {"type": "text", "copy_to": ["all"]},
                "identifier": {"type": "text", "copy_to": ["all"]},
                "name": {"type": "text", "copy_to": ["all"]},
                "role": {"type": "keyword"},
                "title": {"type": "text"},
                "url": {"type": "keyword"},
            }
        },
        "citation": {
            "properties": {
                "@type": {"type": "keyword"},
                "author": {
                    "properties": {
                        "@type": {"type": "text"},
                        "familyName": {"type": "text", "copy_to": ["all"]},
                        "givenName": {"type": "text", "copy_to": ["all"]},
                        "name": {"type": "text", "copy_to": ["all"]},
                    }
                },
                "datePublished": {"type": "date"},
                "doi": {"type": "keyword", "copy_to": ["all"]},
                "identifier": {"type": "keyword", "copy_to": ["all"]},
                "issueNumber": {"type": "text"},
                "journalName": {"type": "keyword", "copy_to": ["all"]},
                "journalNameAbbrev": {"type": "keyword", "copy_to": ["all"]},
                "name": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
                "pagination": {"type": "text"},
                "pmid": {"type": "text", "copy_to": ["all"]},
                "url": {"type": "keyword"},
                "volumeNumber": {"type": "text"},
            }
        },
        "citedBy": {
            "properties": {
                "@type": {"type": "keyword"},
                "abstract": {"type": "text", "analyzer": "nde_analyzer"},
                "citation": {"type": "text"},
                "datePublished": {"type": "date"},
                "description": {"type": "text", "analyzer": "nde_analyzer"},
                "doi": {"type": "text", "copy_to": ["all"]},
                "identifier": {"type": "text", "copy_to": ["all"]},
                "name": {"type": "text", "analyzer": "nde_analyzer"},
                "pmid": {"type": "text", "copy_to": ["all"]},
                "url": {"type": "text"},
            }
        },
        "codeRepository": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "conditionsOfAccess": {"type": "text"},
        "contentUrl": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "contributor": {
            "properties": {
                "@id": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "@type": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "affiliation": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "name": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
            }
        },
        "date": {"type": "date"},
        "dateCreated": {"type": "date"},
        "dateModified": {"type": "date"},
        "datePublished": {"type": "date"},
        "description": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
        "distribution": {
            "properties": {
                "@id": {"type": "keyword"},
                "@type": {"type": "keyword"},
                "contentUrl": {"type": "text"},
                "dateCreated": {"type": "date"},
                "dateModified": {"type": "date"},
                "datePublished": {"type": "date"},
                "description": {"type": "text", "analyzer": "nde_analyzer"},
                "encodingFormat": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "name": {"type": "keyword"},
            }
        },
        "doi": {"type": "text", "copy_to": ["all"]},
        "duration": {"type": "text"},
        "funding": {
            "properties": {
                "description": {"type": "text", "copy_to": ["all"]},
                "funder": {
                    "properties": {
                        "alternateName": {"type": "keyword", "copy_to": ["all"]},
                        "class": {"type": "keyword"},
                        "name": {"type": "keyword", "copy_to": ["all"]},
                        "parentOrganization": {"type": "keyword", "copy_to": ["all"]},
                        "role": {"type": "keyword"},
                        "url": {"type": "text", "copy_to": ["all"]},
                    }
                },
                "identifier": {"type": "text", "copy_to": ["all"]},
                "url": {"type": "text", "copy_to": ["all"]},
            }
        },
        "hasPart": {
            "properties": {
                "@id": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "@type": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
            }
        },
        "healthCondition": {
            "properties": {
                "name": {"type": "keyword", "copy_to": ["all"]},
                "url": {"type": "text", "copy_to": ["all"]},
            }
        },
        "identifier": {"type": "text", "copy_to": ["all"]},
        "input": {
            "properties": {
                "@type": {"type": "keyword"},
                "name": {"type": "text", "copy_to": ["all"]},
                "encodingFormat": {"type": "text", "copy_to": ["all"]},
            },
        },
        "includedInDataCatalog": {
            "properties": {
                "@type": {"type": "text"},
                "name": {"type": "keyword", "copy_to": ["all"]},
                "url": {"type": "text"},
                "versionDate": {"type": "date"},
            }
        },
        "inLanguage": {
            "properties": {
                "@type": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "alternateName": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "name": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
            }
        },
        "infectiousAgent": {
            "properties": {
                "name": {"type": "keyword", "copy_to": ["all"]},
                "url": {"type": "text", "copy_to": ["all"]},
            }
        },
        "interactionStatistic": {
            "properties": {
                "@type": {"type": "text"},
                "interactionType": {"type": "text"},
                "userInteractionCount": {"type": "unsigned_long"}
            }
        },
        "isAvailableForFree": {"type": "boolean"},
        "isBasedOn": {
            "properties": {
                "@type": {"type": "keyword"},
                "abstract": {"type": "text"},
                "citation": {"type": "text"},
                "datePublished": {"type": "date"},
                "description": {"type": "text", "analyzer": "nde_analyzer"},
                "doi": {"type": "text", "copy_to": ["all"]},
                "identifier": {"type": "text", "copy_to": ["all"]},
                "name": {"type": "text", "analyzer": "nde_analyzer"},
                "pmid": {"type": "text", "copy_to": ["all"]},
                "url": {"type": "text"},
            }
        },
        "isPartOf": {
            "properties": {
                "@id": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "@type": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
            }
        },
        "isRelatedTo": {
            "properties": {
                "@type": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "name": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
                "identifier": {"type": "keyword", "copy_to": ["all"]},
                "includedInDataCatalog": {
                    "properties": {
                        "@type": {"type": "text"},
                        "name": {"type": "keyword", "copy_to": ["all"]},
                        "url": {"type": "text"},
                        "versionDate": {"type": "date"},
                    }
                },
                "relationship": {"type": "text", "copy_to": ["all"]}
            }
        },
        "isSimilarTo": {
            "properties": {
                "@type": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "name": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
                "identifier": {"type": "keyword", "copy_to": ["all"]},
                "includedInDataCatalog": {
                    "properties": {
                        "@type": {"type": "text"},
                        "name": {"type": "keyword", "copy_to": ["all"]},
                        "url": {"type": "text"},
                        "versionDate": {"type": "date"},
                    }
                },
                "relationship": {"type": "keyword", "copy_to": ["all"]}
            }
        },
        "keywords": {"type": "keyword", "copy_to": ["all"]},
        "license": {"type": "text"},
        "measurementTechnique": {
            "properties": {
                "name": {"type": "keyword", "copy_to": ["all"]},
                "url": {"type": "text", "copy_to": ["all"]},
            }
        },
        "name": {"type": "keyword", "copy_to": ["all"]},
        "nctid": {"type": "keyword", "copy_to": ["all"]},
        "output": {
            "properties": {
                "@type": {"type": "keyword"},
                "name": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
                "encodingFormat": {"type": "text", "copy_to": ["all"]},
            },
        },
        "relationship": {"type": "text", "copy_to": ["all"]},
        "sameAs": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "sdPublisher": {
            "properties": {
                "@type": {"type": "keyword", "copy_to": ["all"]},
                "identifier": {"type": "text", "copy_to": ["all"]},
                "name": {"type": "text", "copy_to": ["all"]},
                "url": {"type": "keyword"},
            }
        },
        "softwareRequirements": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
        "softwareVersion": {"type": "text", "copy_to": ["all"]},
        "spatialCoverage": {
            "properties": {
                "@type": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "geo": {
                    "properties": {
                        "@type": {
                            "type": "text",
                            "fields": {
                                "keyword": {"type": "keyword", "ignore_above": 256}
                            },
                        },
                        "latitude": {"type": "float"},
                        "longitude": {"type": "float"},
                    }
                },
                "name": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
                "identifier": {
                    "type": "text",
                    "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
                },
            }
        },
        "species": {
            "properties": {
                "name": {"type": "keyword", "copy_to": ["all"]},
                "url": {"type": "text", "copy_to": ["all"]},
            }
        },
        "temporalCoverage": {
            "properties": {
                "temporalInterval": {
                    "properties": {
                        "@type": {"type": "text"},
                        "duration": {"type": "text", "copy_to": ["all"]},
                        "endDate": {"type": "date"},
                        "name": {"type": "text"},
                        "startDate": {"type": "date"},
                    }
                }
            }
        },
        "thumbnailUrl": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "topicCategory": {"type": "keyword", "copy_to": ["all"]},
        "url": {"type": "text", "copy_to": ["all"]},
        "usageInfo": {
            "properties": {
                "description": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
                "name": {"type": "text", "analyzer": "nde_analyzer", "copy_to": ["all"]},
                "url": {"type": "text", "copy_to": ["all"]},
            }
        },
        "variableMeasured": {"type": "keyword", "copy_to": ["all"]},
        "version": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        }
    }

    return mapping
