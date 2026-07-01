from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'geochem_rf_linkml',
     'default_range': 'string',
     'description': 'Warehouse-flavored (star-schema) LinkML schema for the '
                    'ESS-DIVE Sample Data\n'
                    'Reporting Format (Full), targeting a relational data '
                    'lakehouse\n'
                    '(Iceberg/Delta/Parquet).\n'
                    '\n'
                    'This schema has a central `Measurement` fact class '
                    'referencing the dimension classes\n'
                    '`Sample`, `MeasurementVariable`, and `Method` by identifier '
                    '(foreign key), plus\n'
                    'a `Dataset` container holding the fact table and the variable '
                    '"data dictionary"\n'
                    'dimension.',
     'id': 'https://w3id.org/sierra-moxon/geochem-rf-linkml',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'geochem-rf-linkml',
     'prefixes': {'BERVO': {'prefix_prefix': 'BERVO',
                            'prefix_reference': 'https://w3id.org/ber-data/bervo/'},
                  'CUAHSI': {'prefix_prefix': 'CUAHSI',
                             'prefix_reference': 'http://his.cuahsi.org/mastercvreg/VariableNameCV#'},
                  'MIXS': {'prefix_prefix': 'MIXS',
                           'prefix_reference': 'https://w3id.org/mixs/'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'ODM2': {'prefix_prefix': 'ODM2',
                           'prefix_reference': 'http://vocabulary.odm2.org/variablename/'},
                  'STATO': {'prefix_prefix': 'STATO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/STATO_'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'WGS84': {'prefix_prefix': 'WGS84',
                            'prefix_reference': 'http://www.w3.org/2003/01/geo/wgs84_pos#'},
                  'geochem_rf_linkml': {'prefix_prefix': 'geochem_rf_linkml',
                                        'prefix_reference': 'https://w3id.org/sierra-moxon/geochem-rf-linkml/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nmdc': {'prefix_prefix': 'nmdc',
                           'prefix_reference': 'https://w3id.org/nmdc/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'ucum': {'prefix_prefix': 'ucum',
                           'prefix_reference': 'https://ucum.org/ucum#'}},
     'see_also': ['https://sierra-moxon.github.io/geochem-rf-linkml',
                  'https://github.com/ess-dive-community/essdive-sample-data-full'],
     'source_file': 'src/geochem_rf_linkml/schema/geochem_rf_linkml.yaml',
     'title': 'ESS-DIVE Sample Data (Full) Lakehouse Schema'} )

class UnitEnum(str, Enum):
    """
    UCUM-coded units permitted for ESS-DIVE sample-data measurements.
    """
    degree_Celsius = "degree Celsius"
    """
    UCUM: Cel
    """
    microsiemens_per_centimeter = "microsiemens per centimeter"
    """
    UCUM: uS/cm
    """
    milligrams_per_liter = "milligrams per liter"
    """
    UCUM: mg/L
    """
    percent_saturation = "percent saturation"
    """
    UCUM: %{saturation}
    """
    pH = "pH"
    """
    UCUM: [pH]
    """
    moles_per_kilogram = "moles per kilogram"
    """
    UCUM: mol/kg
    """
    moles_per_liter = "moles per liter"
    """
    UCUM: mol/L
    """
    percent = "percent"
    """
    UCUM: %
    """
    per_mille = "per mille"
    """
    UCUM: /10*2
    """
    count = "count"
    """
    UCUM: {count}
    """
    milliliter = "milliliter"
    """
    UCUM: mL
    """
    liter = "liter"
    """
    UCUM: L
    """
    millimeter = "millimeter"
    """
    UCUM: mm
    """
    centimeter = "centimeter"
    """
    UCUM: cm
    """
    meter = "meter"
    """
    UCUM: m
    """
    kilometer = "kilometer"
    """
    UCUM: km
    """
    milligram = "milligram"
    """
    UCUM: mg
    """
    gram = "gram"
    """
    UCUM: g
    """
    kilogram = "kilogram"
    """
    UCUM: kg
    """
    feet_LEFT_PARENTHESISinternationalRIGHT_PARENTHESIS = "feet (international)"
    """
    UCUM: [ft_i]
    """


class DataTypeEnum(str, Enum):
    """
    Data type of the values in a data-file column.
    """
    text = "text"
    numeric = "numeric"
    date = "date"
    datetime = "datetime"


class StatisticEnum(str, Enum):
    """
    Statistic applied to a measured variable (Data Dictionary statistic_*).
    """
    mean = "mean"
    """
    ISO 3534:2006-1 sample mean (arithmetic average).
    """
    minimum = "minimum"
    """
    Minimum value.
    """
    median = "median"
    """
    ISO 3534:2006-1 sample median.
    """
    maximum = "maximum"
    """
    Maximum value.
    """
    total = "total"
    """
    Sum or cumulative amount over the sampling period.
    """
    standard_deviation = "standard deviation"
    """
    ISO 3534:2006-1 (sample) standard deviation.
    """
    standard_error = "standard error"
    """
    ISO 3534:2006-1 standard error of an estimator.
    """
    measurement_uncertainty = "measurement uncertainty"
    """
    JCGM 200:2012 measurement uncertainty.
    """
    R2 = "R2"
    """
    Coefficient of determination.
    """
    RMSE = "RMSE"
    """
    Root mean square error.
    """
    p_value = "p-value"
    """
    ISO 3534:2006-1 p-value.
    """
    CV = "CV"
    """
    ISO 3534:2006-1 sample coefficient of variation.
    """
    covariance = "covariance"
    """
    ISO 3534:2006-1 sample covariance.
    """


class RepresentationTemporalEnum(str, Enum):
    """
    Temporal representation / interval of the measurement.
    """
    year = "year"
    month = "month"
    day = "day"
    number_2_hour = "2-hour"
    hour = "hour"
    number_30_minute = "30-minute"
    number_15_minute = "15-minute"
    number_5_minute = "5-minute"
    minute = "minute"
    second = "second"
    hertz = "hertz"
    other = "other"


class AttrTypeEnum(str, Enum):
    """
    Kind of attribute identified in the Full Methods & Attributes file.
    """
    method_id = "method_id"
    """
    Identifier for method.
    """
    flag_id = "flag_id"
    """
    Identifier for flag.
    """
    treatment_id = "treatment_id"
    """
    Identifier for treatment.
    """
    sensor_id = "sensor_id"
    """
    Identifier for sensor.
    """



class Attribute(ConfiguredBaseModel):
    """
    A domain, measurement, attribute, property, or descriptor for something measured. The identity of *what* is measured (the \"bare concept\", e.g. `temperature`). Mirrors the BERtron/NMDC Attribute pattern: a thin data-dictionary anchor whose `id` is a controlled-vocabulary CURIE.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nmdc:AttributeValue',
         'from_schema': 'https://w3id.org/sierra-moxon/geochem-rf-linkml'})

    id: str = Field(default=..., description="""A unique identifier for a thing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Attribute', 'Dataset'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Human-readable label for the attribute. Where available, the term name from the controlled vocabulary (CUAHSI/ODM2/BERVO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Attribute'], 'slot_uri': 'schema:name'} })


class MeasurementVariable(Attribute):
    """
    A fully-qualified measured variable: the bare `Attribute` concept plus its unit and statistical/temporal qualifiers. One row of the ESS-DIVE Data Dictionary. This is the \"variable dimension\" of the star schema; the dimension business key is the qualified-identity tuple (see `unique_keys`), NOT the arbitrary user column name.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/geochem-rf-linkml',
         'slot_usage': {'definition': {'name': 'definition', 'required': True},
                        'id': {'description': 'CURIE for the qualified variable (or '
                                              'its underlying CUAHSI/ODM2/BERVO term). '
                                              'Serves as the dimension key / '
                                              'foreign-key target.',
                               'identifier': True,
                               'name': 'id'},
                        'unit': {'name': 'unit',
                                 'range': 'UnitEnum',
                                 'required': True}},
         'unique_keys': {'variable_identity': {'description': 'dedups the conformed '
                                                              'variable: two '
                                                              'differently-named '
                                                              'columns with the same '
                                                              'qualified tuple are the '
                                                              'SAME '
                                                              'MeasurementVariable '
                                                              '(attacks soil_ph vs '
                                                              'soil_p_h).',
                                               'unique_key_name': 'variable_identity',
                                               'unique_key_slots': ['label',
                                                                    'unit',
                                                                    'unit_basis',
                                                                    'statistic_measurement',
                                                                    'statistic_spatial',
                                                                    'statistic_temporal',
                                                                    'representation_temporal']}}})

    unit: UnitEnum = Field(default=..., description="""UCUM-coded unit of the measurement (Data Dictionary `unit`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    unit_cv_id: Optional[str] = Field(default=None, description="""The unit expressed as an ontology CURIE (e.g. UO / UCUM).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    definition: str = Field(default=..., description="""Definition of the measured variable (Data Dictionary `definition`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable'], 'slot_uri': 'schema:description'} })
    data_type: Optional[DataTypeEnum] = Field(default=None, description="""Data type of the values (Data Dictionary `data_type`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    unit_basis: Optional[str] = Field(default=None, description="""Basis for the reported unit (e.g. dry weight), Data Dictionary `unit_basis`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    missing_value_code: Optional[str] = Field(default=None, description="""Code used in the data file to indicate a missing value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    statistic_measurement: Optional[StatisticEnum] = Field(default=None, description="""Statistic applied across measurements (Data Dictionary `statistic_measurement`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    statistic_spatial: Optional[StatisticEnum] = Field(default=None, description="""Statistic applied across space (Data Dictionary `statistic_spatial`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    statistic_temporal: Optional[StatisticEnum] = Field(default=None, description="""Statistic applied across time (Data Dictionary `statistic_temporal`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    representation_temporal: Optional[RepresentationTemporalEnum] = Field(default=None, description="""Temporal representation / interval (Data Dictionary `representation_temporal`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    lower_bound: Optional[float] = Field(default=None, description="""Lower plausibility/validity bound for the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable', 'Method']} })
    upper_bound: Optional[float] = Field(default=None, description="""Upper plausibility/validity bound for the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable', 'Method']} })
    column_or_row_name: Optional[str] = Field(default=None, description="""The arbitrary user-supplied column (or row) label from the source data file. NOT an identity -- kept only as a non-identifying alias.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    column_or_row_long_name: Optional[str] = Field(default=None, description="""Optional long-form name for the column/row.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable']} })
    id: str = Field(default=..., description="""CURIE for the qualified variable (or its underlying CUAHSI/ODM2/BERVO term). Serves as the dimension key / foreign-key target.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Attribute', 'Dataset'], 'slot_uri': 'schema:identifier'} })
    label: str = Field(default=..., description="""Human-readable label for the attribute. Where available, the term name from the controlled vocabulary (CUAHSI/ODM2/BERVO).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Attribute'], 'slot_uri': 'schema:name'} })


class Sample(ConfiguredBaseModel):
    """
    A physical sample (or a time point on a sample) that measurements are made on. The sample dimension of the star schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/geochem-rf-linkml',
         'slot_usage': {'sample_name': {'identifier': True,
                                        'name': 'sample_name',
                                        'required': True}}})

    sample_name: str = Field(default=..., description="""Name/identifier of the physical sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    datetime_collected: Optional[datetime ] = Field(default=None, description="""Date/time the sample was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    latitude: Optional[float] = Field(default=None, description="""Latitude (WGS84 decimal degrees).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'WGS84:lat'} })
    longitude: Optional[float] = Field(default=None, description="""Longitude (WGS84 decimal degrees).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample'], 'slot_uri': 'WGS84:long'} })
    location_description: Optional[str] = Field(default=None, description="""Free-text description of the sampling location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })


class Method(ConfiguredBaseModel):
    """
    One row of the Full \"Methods & Attributes\" file (`*_sample_attr.csv`): the method/flag/treatment/sensor definition referenced per-measurement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/geochem-rf-linkml',
         'slot_usage': {'attr_description': {'name': 'attr_description',
                                             'required': True},
                        'attr_id': {'identifier': True,
                                    'name': 'attr_id',
                                    'required': True},
                        'attr_type': {'name': 'attr_type',
                                      'range': 'AttrTypeEnum',
                                      'required': True}},
         'unique_keys': {'attr_key': {'description': 'Composite unique key from the '
                                                     'Full RF.',
                                      'unique_key_name': 'attr_key',
                                      'unique_key_slots': ['attr_id', 'attr_type']}}})

    attr_id: str = Field(default=..., description="""Identifier for a method/flag/treatment/sensor (Methods & Attributes `attr_id`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    attr_type: AttrTypeEnum = Field(default=..., description="""Kind of attribute identified by `attr_id`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    attr_description: str = Field(default=..., description="""Description of the method/flag/treatment/sensor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    analysis_detection_limit: Optional[float] = Field(default=None, description="""Analysis detection limit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    analysis_precision: Optional[float] = Field(default=None, description="""Analysis precision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    instrument_precision: Optional[float] = Field(default=None, description="""Instrument precision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    lower_bound: Optional[float] = Field(default=None, description="""Lower plausibility/validity bound for the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable', 'Method']} })
    upper_bound: Optional[float] = Field(default=None, description="""Upper plausibility/validity bound for the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementVariable', 'Method']} })
    method_instrument: Optional[str] = Field(default=None, description="""Instrument used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_reference: Optional[str] = Field(default=None, description="""Citation/reference for the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_hold_time: Optional[str] = Field(default=None, description="""Sample hold time before analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_temp: Optional[str] = Field(default=None, description="""Temperature condition of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_light: Optional[str] = Field(default=None, description="""Light condition of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_atmosphere: Optional[str] = Field(default=None, description="""Atmospheric condition of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_moisture: Optional[str] = Field(default=None, description="""Moisture condition of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_medium: Optional[str] = Field(default=None, description="""Medium of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_time: Optional[str] = Field(default=None, description="""Timing detail of the method.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_lab_contact: Optional[str] = Field(default=None, description="""Laboratory contact.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_instrument_operator: Optional[str] = Field(default=None, description="""Instrument operator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })
    method_lab: Optional[str] = Field(default=None, description="""Laboratory that performed the analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Method']} })


class Measurement(ConfiguredBaseModel):
    """
    A single measured value: the \"fact\" of the star schema. Points at a `Sample` and a `MeasurementVariable` (and optionally a `Method`) by identifier, and carries the actual measure(s).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/geochem-rf-linkml',
         'slot_usage': {'method': {'inlined': False,
                                   'multivalued': True,
                                   'name': 'method',
                                   'range': 'Method'},
                        'numeric_value': {'name': 'numeric_value', 'range': 'float'},
                        'sample': {'inlined': False,
                                   'name': 'sample',
                                   'range': 'Sample',
                                   'required': True},
                        'variable': {'inlined': False,
                                     'name': 'variable',
                                     'range': 'MeasurementVariable',
                                     'required': True}}})

    sample: str = Field(default=..., description="""Foreign key to the sample dimension.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    variable: str = Field(default=..., description="""Foreign key to the variable dimension.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    method: Optional[list[str]] = Field(default=None, description="""Foreign key to the method dimension (Full RF).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    numeric_value: Optional[float] = Field(default=None, description="""The numeric measure (kept typed for Parquet stats / pushdown).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'nmdc:numeric_value'} })
    string_value: Optional[str] = Field(default=None, description="""The measure when it is textual (typed EAV column, sparse).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    datetime_value: Optional[datetime ] = Field(default=None, description="""The measure when it is a date/time (typed EAV column, sparse).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    raw_value: Optional[str] = Field(default=None, description="""The unnormalized atomic string as reported (e.g. \"2.2 mg/L\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'nmdc:raw_value'} })
    flag: Optional[list[str]] = Field(default=None, description="""Quality/other flags for the measurement (`{...}_flag`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    treatment_id: Optional[str] = Field(default=None, description="""Treatment identifier applied to this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    datetime_measured: Optional[datetime ] = Field(default=None, description="""Date/time the measurement was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    time_elapsed: Optional[float] = Field(default=None, description="""Elapsed time for a time-series measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })


class Dataset(ConfiguredBaseModel):
    """
    A single ESS-DIVE sample-data package: the whole `Measurement` fact table plus the `MeasurementVariable` data-dictionary dimension (and the sample / method dimensions).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/geochem-rf-linkml',
         'slot_usage': {'measurements': {'inlined_as_list': True,
                                         'multivalued': True,
                                         'name': 'measurements',
                                         'range': 'Measurement'},
                        'methods': {'inlined_as_list': True,
                                    'multivalued': True,
                                    'name': 'methods',
                                    'range': 'Method'},
                        'samples': {'inlined_as_list': True,
                                    'multivalued': True,
                                    'name': 'samples',
                                    'range': 'Sample'},
                        'variables': {'inlined_as_list': True,
                                      'multivalued': True,
                                      'name': 'variables',
                                      'range': 'MeasurementVariable'}},
         'tree_root': True})

    id: str = Field(default=..., description="""A unique identifier for a thing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Attribute', 'Dataset'], 'slot_uri': 'schema:identifier'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for a thing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:name'} })
    measurements: Optional[list[Measurement]] = Field(default=None, description="""The measurement fact table for the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    variables: Optional[list[MeasurementVariable]] = Field(default=None, description="""The variable dimension (the data dictionary) for the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    samples: Optional[list[Sample]] = Field(default=None, description="""The sample dimension for the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    methods: Optional[list[Method]] = Field(default=None, description="""The method dimension for the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Attribute.model_rebuild()
MeasurementVariable.model_rebuild()
Sample.model_rebuild()
Method.model_rebuild()
Measurement.model_rebuild()
Dataset.model_rebuild()
