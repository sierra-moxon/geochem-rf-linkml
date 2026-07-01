# Auto generated from geochem_rf_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-30T18:25:56
# Schema: geochem-rf-linkml
#
# id: https://w3id.org/sierra-moxon/geochem-rf-linkml
# description: Warehouse-flavored (star-schema) LinkML schema for the ESS-DIVE Sample Data
#   Reporting Format (Full), targeting a relational data lakehouse
#   (Iceberg/Delta/Parquet).
#
#   This schema has a central `Measurement` fact class referencing the dimension classes
#   `Sample`, `MeasurementVariable`, and `Method` by identifier (foreign key), plus
#   a `Dataset` container holding the fact table and the variable "data dictionary"
#   dimension.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Float, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDateTime

metamodel_version = "1.11.0"
version = None

# Namespaces
BERVO = CurieNamespace('BERVO', 'https://w3id.org/ber-data/bervo/')
CUAHSI = CurieNamespace('CUAHSI', 'http://his.cuahsi.org/mastercvreg/VariableNameCV#')
MIXS = CurieNamespace('MIXS', 'https://w3id.org/mixs/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
ODM2 = CurieNamespace('ODM2', 'http://vocabulary.odm2.org/variablename/')
STATO = CurieNamespace('STATO', 'http://purl.obolibrary.org/obo/STATO_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
WGS84 = CurieNamespace('WGS84', 'http://www.w3.org/2003/01/geo/wgs84_pos#')
GEOCHEM_RF_LINKML = CurieNamespace('geochem_rf_linkml', 'https://w3id.org/sierra-moxon/geochem-rf-linkml/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
UCUM = CurieNamespace('ucum', 'https://ucum.org/ucum#')
DEFAULT_ = GEOCHEM_RF_LINKML


# Types

# Class references
class AttributeId(URIorCURIE):
    pass


class MeasurementVariableId(AttributeId):
    pass


class SampleSampleName(extended_str):
    pass


class MethodAttrId(extended_str):
    pass


class DatasetId(URIorCURIE):
    pass


@dataclass(repr=False)
class Attribute(YAMLRoot):
    """
    A domain, measurement, attribute, property, or descriptor for something measured. The identity of *what* is
    measured (the "bare concept", e.g. `temperature`). Mirrors the BERtron/NMDC Attribute pattern: a thin
    data-dictionary anchor whose `id` is a controlled-vocabulary CURIE.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["AttributeValue"]
    class_class_curie: ClassVar[str] = "nmdc:AttributeValue"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML.Attribute

    id: Union[str, AttributeId] = None
    label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AttributeId):
            self.id = AttributeId(self.id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasurementVariable(Attribute):
    """
    A fully-qualified measured variable: the bare `Attribute` concept plus its unit and statistical/temporal
    qualifiers. One row of the ESS-DIVE Data Dictionary. This is the "variable dimension" of the star schema; the
    dimension business key is the qualified-identity tuple (see `unique_keys`), NOT the arbitrary user column name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML["MeasurementVariable"]
    class_class_curie: ClassVar[str] = "geochem_rf_linkml:MeasurementVariable"
    class_name: ClassVar[str] = "MeasurementVariable"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML.MeasurementVariable

    id: Union[str, MeasurementVariableId] = None
    label: str = None
    unit: Union[str, "UnitEnum"] = None
    definition: str = None
    unit_cv_id: Optional[Union[str, URIorCURIE]] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    unit_basis: Optional[str] = None
    missing_value_code: Optional[str] = None
    statistic_measurement: Optional[Union[str, "StatisticEnum"]] = None
    statistic_spatial: Optional[Union[str, "StatisticEnum"]] = None
    statistic_temporal: Optional[Union[str, "StatisticEnum"]] = None
    representation_temporal: Optional[Union[str, "RepresentationTemporalEnum"]] = None
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    column_or_row_name: Optional[str] = None
    column_or_row_long_name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementVariableId):
            self.id = MeasurementVariableId(self.id)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, UnitEnum):
            self.unit = UnitEnum(self.unit)

        if self._is_empty(self.definition):
            self.MissingRequiredField("definition")
        if not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.unit_cv_id is not None and not isinstance(self.unit_cv_id, URIorCURIE):
            self.unit_cv_id = URIorCURIE(self.unit_cv_id)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeEnum):
            self.data_type = DataTypeEnum(self.data_type)

        if self.unit_basis is not None and not isinstance(self.unit_basis, str):
            self.unit_basis = str(self.unit_basis)

        if self.missing_value_code is not None and not isinstance(self.missing_value_code, str):
            self.missing_value_code = str(self.missing_value_code)

        if self.statistic_measurement is not None and not isinstance(self.statistic_measurement, StatisticEnum):
            self.statistic_measurement = StatisticEnum(self.statistic_measurement)

        if self.statistic_spatial is not None and not isinstance(self.statistic_spatial, StatisticEnum):
            self.statistic_spatial = StatisticEnum(self.statistic_spatial)

        if self.statistic_temporal is not None and not isinstance(self.statistic_temporal, StatisticEnum):
            self.statistic_temporal = StatisticEnum(self.statistic_temporal)

        if self.representation_temporal is not None and not isinstance(self.representation_temporal, RepresentationTemporalEnum):
            self.representation_temporal = RepresentationTemporalEnum(self.representation_temporal)

        if self.lower_bound is not None and not isinstance(self.lower_bound, float):
            self.lower_bound = float(self.lower_bound)

        if self.upper_bound is not None and not isinstance(self.upper_bound, float):
            self.upper_bound = float(self.upper_bound)

        if self.column_or_row_name is not None and not isinstance(self.column_or_row_name, str):
            self.column_or_row_name = str(self.column_or_row_name)

        if self.column_or_row_long_name is not None and not isinstance(self.column_or_row_long_name, str):
            self.column_or_row_long_name = str(self.column_or_row_long_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    A physical sample (or a time point on a sample) that measurements are made on. The sample dimension of the star
    schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML["Sample"]
    class_class_curie: ClassVar[str] = "geochem_rf_linkml:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML.Sample

    sample_name: Union[str, SampleSampleName] = None
    datetime_collected: Optional[Union[str, XSDDateTime]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    location_description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sample_name):
            self.MissingRequiredField("sample_name")
        if not isinstance(self.sample_name, SampleSampleName):
            self.sample_name = SampleSampleName(self.sample_name)

        if self.datetime_collected is not None and not isinstance(self.datetime_collected, XSDDateTime):
            self.datetime_collected = XSDDateTime(self.datetime_collected)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.location_description is not None and not isinstance(self.location_description, str):
            self.location_description = str(self.location_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Method(YAMLRoot):
    """
    One row of the Full "Methods & Attributes" file (`*_sample_attr.csv`): the method/flag/treatment/sensor definition
    referenced per-measurement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML["Method"]
    class_class_curie: ClassVar[str] = "geochem_rf_linkml:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML.Method

    attr_id: Union[str, MethodAttrId] = None
    attr_type: Union[str, "AttrTypeEnum"] = None
    attr_description: str = None
    analysis_detection_limit: Optional[float] = None
    analysis_precision: Optional[float] = None
    instrument_precision: Optional[float] = None
    lower_bound: Optional[float] = None
    upper_bound: Optional[float] = None
    method_instrument: Optional[str] = None
    method_reference: Optional[str] = None
    method_hold_time: Optional[str] = None
    method_temp: Optional[str] = None
    method_light: Optional[str] = None
    method_atmosphere: Optional[str] = None
    method_moisture: Optional[str] = None
    method_medium: Optional[str] = None
    method_time: Optional[str] = None
    method_lab_contact: Optional[str] = None
    method_instrument_operator: Optional[str] = None
    method_lab: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.attr_id):
            self.MissingRequiredField("attr_id")
        if not isinstance(self.attr_id, MethodAttrId):
            self.attr_id = MethodAttrId(self.attr_id)

        if self._is_empty(self.attr_type):
            self.MissingRequiredField("attr_type")
        if not isinstance(self.attr_type, AttrTypeEnum):
            self.attr_type = AttrTypeEnum(self.attr_type)

        if self._is_empty(self.attr_description):
            self.MissingRequiredField("attr_description")
        if not isinstance(self.attr_description, str):
            self.attr_description = str(self.attr_description)

        if self.analysis_detection_limit is not None and not isinstance(self.analysis_detection_limit, float):
            self.analysis_detection_limit = float(self.analysis_detection_limit)

        if self.analysis_precision is not None and not isinstance(self.analysis_precision, float):
            self.analysis_precision = float(self.analysis_precision)

        if self.instrument_precision is not None and not isinstance(self.instrument_precision, float):
            self.instrument_precision = float(self.instrument_precision)

        if self.lower_bound is not None and not isinstance(self.lower_bound, float):
            self.lower_bound = float(self.lower_bound)

        if self.upper_bound is not None and not isinstance(self.upper_bound, float):
            self.upper_bound = float(self.upper_bound)

        if self.method_instrument is not None and not isinstance(self.method_instrument, str):
            self.method_instrument = str(self.method_instrument)

        if self.method_reference is not None and not isinstance(self.method_reference, str):
            self.method_reference = str(self.method_reference)

        if self.method_hold_time is not None and not isinstance(self.method_hold_time, str):
            self.method_hold_time = str(self.method_hold_time)

        if self.method_temp is not None and not isinstance(self.method_temp, str):
            self.method_temp = str(self.method_temp)

        if self.method_light is not None and not isinstance(self.method_light, str):
            self.method_light = str(self.method_light)

        if self.method_atmosphere is not None and not isinstance(self.method_atmosphere, str):
            self.method_atmosphere = str(self.method_atmosphere)

        if self.method_moisture is not None and not isinstance(self.method_moisture, str):
            self.method_moisture = str(self.method_moisture)

        if self.method_medium is not None and not isinstance(self.method_medium, str):
            self.method_medium = str(self.method_medium)

        if self.method_time is not None and not isinstance(self.method_time, str):
            self.method_time = str(self.method_time)

        if self.method_lab_contact is not None and not isinstance(self.method_lab_contact, str):
            self.method_lab_contact = str(self.method_lab_contact)

        if self.method_instrument_operator is not None and not isinstance(self.method_instrument_operator, str):
            self.method_instrument_operator = str(self.method_instrument_operator)

        if self.method_lab is not None and not isinstance(self.method_lab, str):
            self.method_lab = str(self.method_lab)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Measurement(YAMLRoot):
    """
    A single measured value: the "fact" of the star schema. Points at a `Sample` and a `MeasurementVariable` (and
    optionally a `Method`) by identifier, and carries the actual measure(s).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML["Measurement"]
    class_class_curie: ClassVar[str] = "geochem_rf_linkml:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML.Measurement

    sample: Union[str, SampleSampleName] = None
    variable: Union[str, MeasurementVariableId] = None
    method: Optional[Union[Union[str, MethodAttrId], list[Union[str, MethodAttrId]]]] = empty_list()
    numeric_value: Optional[float] = None
    string_value: Optional[str] = None
    datetime_value: Optional[Union[str, XSDDateTime]] = None
    raw_value: Optional[str] = None
    flag: Optional[Union[str, list[str]]] = empty_list()
    treatment_id: Optional[str] = None
    datetime_measured: Optional[Union[str, XSDDateTime]] = None
    time_elapsed: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sample):
            self.MissingRequiredField("sample")
        if not isinstance(self.sample, SampleSampleName):
            self.sample = SampleSampleName(self.sample)

        if self._is_empty(self.variable):
            self.MissingRequiredField("variable")
        if not isinstance(self.variable, MeasurementVariableId):
            self.variable = MeasurementVariableId(self.variable)

        if not isinstance(self.method, list):
            self.method = [self.method] if self.method is not None else []
        self.method = [v if isinstance(v, MethodAttrId) else MethodAttrId(v) for v in self.method]

        if self.numeric_value is not None and not isinstance(self.numeric_value, float):
            self.numeric_value = float(self.numeric_value)

        if self.string_value is not None and not isinstance(self.string_value, str):
            self.string_value = str(self.string_value)

        if self.datetime_value is not None and not isinstance(self.datetime_value, XSDDateTime):
            self.datetime_value = XSDDateTime(self.datetime_value)

        if self.raw_value is not None and not isinstance(self.raw_value, str):
            self.raw_value = str(self.raw_value)

        if not isinstance(self.flag, list):
            self.flag = [self.flag] if self.flag is not None else []
        self.flag = [v if isinstance(v, str) else str(v) for v in self.flag]

        if self.treatment_id is not None and not isinstance(self.treatment_id, str):
            self.treatment_id = str(self.treatment_id)

        if self.datetime_measured is not None and not isinstance(self.datetime_measured, XSDDateTime):
            self.datetime_measured = XSDDateTime(self.datetime_measured)

        if self.time_elapsed is not None and not isinstance(self.time_elapsed, float):
            self.time_elapsed = float(self.time_elapsed)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A single ESS-DIVE sample-data package: the whole `Measurement` fact table plus the `MeasurementVariable`
    data-dictionary dimension (and the sample / method dimensions).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML["Dataset"]
    class_class_curie: ClassVar[str] = "geochem_rf_linkml:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = GEOCHEM_RF_LINKML.Dataset

    id: Union[str, DatasetId] = None
    name: Optional[str] = None
    measurements: Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]] = empty_list()
    variables: Optional[Union[dict[Union[str, MeasurementVariableId], Union[dict, MeasurementVariable]], list[Union[dict, MeasurementVariable]]]] = empty_dict()
    samples: Optional[Union[dict[Union[str, SampleSampleName], Union[dict, Sample]], list[Union[dict, Sample]]]] = empty_dict()
    methods: Optional[Union[dict[Union[str, MethodAttrId], Union[dict, Method]], list[Union[dict, Method]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.measurements, list):
            self.measurements = [self.measurements] if self.measurements is not None else []
        self.measurements = [v if isinstance(v, Measurement) else Measurement(**as_dict(v)) for v in self.measurements]

        self._normalize_inlined_as_list(slot_name="variables", slot_type=MeasurementVariable, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="sample_name", keyed=True)

        self._normalize_inlined_as_list(slot_name="methods", slot_type=Method, key_name="attr_id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class UnitEnum(EnumDefinitionImpl):
    """
    UCUM-coded units permitted for ESS-DIVE sample-data measurements.
    """
    pH = PermissibleValue(
        text="pH",
        description="UCUM: [pH]")
    percent = PermissibleValue(
        text="percent",
        description="UCUM: %")
    count = PermissibleValue(
        text="count",
        description="UCUM: {count}")
    milliliter = PermissibleValue(
        text="milliliter",
        description="UCUM: mL",
        meaning=UCUM["mL"])
    liter = PermissibleValue(
        text="liter",
        description="UCUM: L",
        meaning=UCUM["L"])
    millimeter = PermissibleValue(
        text="millimeter",
        description="UCUM: mm",
        meaning=UCUM["mm"])
    centimeter = PermissibleValue(
        text="centimeter",
        description="UCUM: cm",
        meaning=UCUM["cm"])
    meter = PermissibleValue(
        text="meter",
        description="UCUM: m",
        meaning=UCUM["m"])
    kilometer = PermissibleValue(
        text="kilometer",
        description="UCUM: km",
        meaning=UCUM["km"])
    milligram = PermissibleValue(
        text="milligram",
        description="UCUM: mg",
        meaning=UCUM["mg"])
    gram = PermissibleValue(
        text="gram",
        description="UCUM: g",
        meaning=UCUM["g"])
    kilogram = PermissibleValue(
        text="kilogram",
        description="UCUM: kg",
        meaning=UCUM["kg"])

    _defn = EnumDefinition(
        name="UnitEnum",
        description="UCUM-coded units permitted for ESS-DIVE sample-data measurements.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "degree Celsius",
            PermissibleValue(
                text="degree Celsius",
                description="UCUM: Cel",
                meaning=UCUM["Cel"]))
        setattr(cls, "microsiemens per centimeter",
            PermissibleValue(
                text="microsiemens per centimeter",
                description="UCUM: uS/cm",
                meaning=UCUM["uS/cm"]))
        setattr(cls, "milligrams per liter",
            PermissibleValue(
                text="milligrams per liter",
                description="UCUM: mg/L",
                meaning=UCUM["mg/L"]))
        setattr(cls, "percent saturation",
            PermissibleValue(
                text="percent saturation",
                description="UCUM: %{saturation}"))
        setattr(cls, "moles per kilogram",
            PermissibleValue(
                text="moles per kilogram",
                description="UCUM: mol/kg",
                meaning=UCUM["mol/kg"]))
        setattr(cls, "moles per liter",
            PermissibleValue(
                text="moles per liter",
                description="UCUM: mol/L",
                meaning=UCUM["mol/L"]))
        setattr(cls, "per mille",
            PermissibleValue(
                text="per mille",
                description="UCUM: /10*2"))
        setattr(cls, "feet (international)",
            PermissibleValue(
                text="feet (international)",
                description="UCUM: [ft_i]"))

class DataTypeEnum(EnumDefinitionImpl):
    """
    Data type of the values in a data-file column.
    """
    text = PermissibleValue(text="text")
    numeric = PermissibleValue(text="numeric")
    date = PermissibleValue(text="date")
    datetime = PermissibleValue(text="datetime")

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Data type of the values in a data-file column.",
    )

class StatisticEnum(EnumDefinitionImpl):
    """
    Statistic applied to a measured variable (Data Dictionary statistic_*).
    """
    mean = PermissibleValue(
        text="mean",
        description="ISO 3534:2006-1 sample mean (arithmetic average).",
        meaning=STATO["0000401"])
    minimum = PermissibleValue(
        text="minimum",
        description="Minimum value.")
    median = PermissibleValue(
        text="median",
        description="ISO 3534:2006-1 sample median.",
        meaning=STATO["0000574"])
    maximum = PermissibleValue(
        text="maximum",
        description="Maximum value.")
    total = PermissibleValue(
        text="total",
        description="Sum or cumulative amount over the sampling period.")
    R2 = PermissibleValue(
        text="R2",
        description="Coefficient of determination.")
    RMSE = PermissibleValue(
        text="RMSE",
        description="Root mean square error.")
    CV = PermissibleValue(
        text="CV",
        description="ISO 3534:2006-1 sample coefficient of variation.")
    covariance = PermissibleValue(
        text="covariance",
        description="ISO 3534:2006-1 sample covariance.")

    _defn = EnumDefinition(
        name="StatisticEnum",
        description="Statistic applied to a measured variable (Data Dictionary statistic_*).",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "standard deviation",
            PermissibleValue(
                text="standard deviation",
                description="ISO 3534:2006-1 (sample) standard deviation.",
                meaning=STATO["0000237"]))
        setattr(cls, "standard error",
            PermissibleValue(
                text="standard error",
                description="ISO 3534:2006-1 standard error of an estimator."))
        setattr(cls, "measurement uncertainty",
            PermissibleValue(
                text="measurement uncertainty",
                description="JCGM 200:2012 measurement uncertainty."))
        setattr(cls, "p-value",
            PermissibleValue(
                text="p-value",
                description="ISO 3534:2006-1 p-value.",
                meaning=STATO["0000700"]))

class RepresentationTemporalEnum(EnumDefinitionImpl):
    """
    Temporal representation / interval of the measurement.
    """
    year = PermissibleValue(text="year")
    month = PermissibleValue(text="month")
    day = PermissibleValue(text="day")
    hour = PermissibleValue(text="hour")
    minute = PermissibleValue(text="minute")
    second = PermissibleValue(text="second")
    hertz = PermissibleValue(text="hertz")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="RepresentationTemporalEnum",
        description="Temporal representation / interval of the measurement.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "2-hour",
            PermissibleValue(text="2-hour"))
        setattr(cls, "30-minute",
            PermissibleValue(text="30-minute"))
        setattr(cls, "15-minute",
            PermissibleValue(text="15-minute"))
        setattr(cls, "5-minute",
            PermissibleValue(text="5-minute"))

class AttrTypeEnum(EnumDefinitionImpl):
    """
    Kind of attribute identified in the Full Methods & Attributes file.
    """
    method_id = PermissibleValue(
        text="method_id",
        description="Identifier for method.")
    flag_id = PermissibleValue(
        text="flag_id",
        description="Identifier for flag.")
    treatment_id = PermissibleValue(
        text="treatment_id",
        description="Identifier for treatment.")
    sensor_id = PermissibleValue(
        text="sensor_id",
        description="Identifier for sensor.")

    _defn = EnumDefinition(
        name="AttrTypeEnum",
        description="Kind of attribute identified in the Full Methods & Attributes file.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=GEOCHEM_RF_LINKML.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=GEOCHEM_RF_LINKML.name, domain=None, range=Optional[str])

slots.label = Slot(uri=SCHEMA.name, name="label", curie=SCHEMA.curie('name'),
                   model_uri=GEOCHEM_RF_LINKML.label, domain=None, range=str)

slots.definition = Slot(uri=SCHEMA.description, name="definition", curie=SCHEMA.curie('description'),
                   model_uri=GEOCHEM_RF_LINKML.definition, domain=None, range=Optional[str])

slots.column_or_row_name = Slot(uri=GEOCHEM_RF_LINKML.column_or_row_name, name="column_or_row_name", curie=GEOCHEM_RF_LINKML.curie('column_or_row_name'),
                   model_uri=GEOCHEM_RF_LINKML.column_or_row_name, domain=None, range=Optional[str])

slots.column_or_row_long_name = Slot(uri=GEOCHEM_RF_LINKML.column_or_row_long_name, name="column_or_row_long_name", curie=GEOCHEM_RF_LINKML.curie('column_or_row_long_name'),
                   model_uri=GEOCHEM_RF_LINKML.column_or_row_long_name, domain=None, range=Optional[str])

slots.unit = Slot(uri=GEOCHEM_RF_LINKML.unit, name="unit", curie=GEOCHEM_RF_LINKML.curie('unit'),
                   model_uri=GEOCHEM_RF_LINKML.unit, domain=None, range=Optional[Union[str, "UnitEnum"]])

slots.unit_cv_id = Slot(uri=GEOCHEM_RF_LINKML.unit_cv_id, name="unit_cv_id", curie=GEOCHEM_RF_LINKML.curie('unit_cv_id'),
                   model_uri=GEOCHEM_RF_LINKML.unit_cv_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.unit_basis = Slot(uri=GEOCHEM_RF_LINKML.unit_basis, name="unit_basis", curie=GEOCHEM_RF_LINKML.curie('unit_basis'),
                   model_uri=GEOCHEM_RF_LINKML.unit_basis, domain=None, range=Optional[str])

slots.data_type = Slot(uri=GEOCHEM_RF_LINKML.data_type, name="data_type", curie=GEOCHEM_RF_LINKML.curie('data_type'),
                   model_uri=GEOCHEM_RF_LINKML.data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.missing_value_code = Slot(uri=GEOCHEM_RF_LINKML.missing_value_code, name="missing_value_code", curie=GEOCHEM_RF_LINKML.curie('missing_value_code'),
                   model_uri=GEOCHEM_RF_LINKML.missing_value_code, domain=None, range=Optional[str])

slots.statistic_measurement = Slot(uri=GEOCHEM_RF_LINKML.statistic_measurement, name="statistic_measurement", curie=GEOCHEM_RF_LINKML.curie('statistic_measurement'),
                   model_uri=GEOCHEM_RF_LINKML.statistic_measurement, domain=None, range=Optional[Union[str, "StatisticEnum"]])

slots.statistic_spatial = Slot(uri=GEOCHEM_RF_LINKML.statistic_spatial, name="statistic_spatial", curie=GEOCHEM_RF_LINKML.curie('statistic_spatial'),
                   model_uri=GEOCHEM_RF_LINKML.statistic_spatial, domain=None, range=Optional[Union[str, "StatisticEnum"]])

slots.statistic_temporal = Slot(uri=GEOCHEM_RF_LINKML.statistic_temporal, name="statistic_temporal", curie=GEOCHEM_RF_LINKML.curie('statistic_temporal'),
                   model_uri=GEOCHEM_RF_LINKML.statistic_temporal, domain=None, range=Optional[Union[str, "StatisticEnum"]])

slots.representation_temporal = Slot(uri=GEOCHEM_RF_LINKML.representation_temporal, name="representation_temporal", curie=GEOCHEM_RF_LINKML.curie('representation_temporal'),
                   model_uri=GEOCHEM_RF_LINKML.representation_temporal, domain=None, range=Optional[Union[str, "RepresentationTemporalEnum"]])

slots.lower_bound = Slot(uri=GEOCHEM_RF_LINKML.lower_bound, name="lower_bound", curie=GEOCHEM_RF_LINKML.curie('lower_bound'),
                   model_uri=GEOCHEM_RF_LINKML.lower_bound, domain=None, range=Optional[float])

slots.upper_bound = Slot(uri=GEOCHEM_RF_LINKML.upper_bound, name="upper_bound", curie=GEOCHEM_RF_LINKML.curie('upper_bound'),
                   model_uri=GEOCHEM_RF_LINKML.upper_bound, domain=None, range=Optional[float])

slots.sample_name = Slot(uri=GEOCHEM_RF_LINKML.sample_name, name="sample_name", curie=GEOCHEM_RF_LINKML.curie('sample_name'),
                   model_uri=GEOCHEM_RF_LINKML.sample_name, domain=None, range=Optional[str])

slots.datetime_collected = Slot(uri=GEOCHEM_RF_LINKML.datetime_collected, name="datetime_collected", curie=GEOCHEM_RF_LINKML.curie('datetime_collected'),
                   model_uri=GEOCHEM_RF_LINKML.datetime_collected, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.latitude = Slot(uri=WGS84.lat, name="latitude", curie=WGS84.curie('lat'),
                   model_uri=GEOCHEM_RF_LINKML.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=WGS84.long, name="longitude", curie=WGS84.curie('long'),
                   model_uri=GEOCHEM_RF_LINKML.longitude, domain=None, range=Optional[float])

slots.location_description = Slot(uri=GEOCHEM_RF_LINKML.location_description, name="location_description", curie=GEOCHEM_RF_LINKML.curie('location_description'),
                   model_uri=GEOCHEM_RF_LINKML.location_description, domain=None, range=Optional[str])

slots.attr_id = Slot(uri=GEOCHEM_RF_LINKML.attr_id, name="attr_id", curie=GEOCHEM_RF_LINKML.curie('attr_id'),
                   model_uri=GEOCHEM_RF_LINKML.attr_id, domain=None, range=Optional[str])

slots.attr_type = Slot(uri=GEOCHEM_RF_LINKML.attr_type, name="attr_type", curie=GEOCHEM_RF_LINKML.curie('attr_type'),
                   model_uri=GEOCHEM_RF_LINKML.attr_type, domain=None, range=Optional[Union[str, "AttrTypeEnum"]])

slots.attr_description = Slot(uri=GEOCHEM_RF_LINKML.attr_description, name="attr_description", curie=GEOCHEM_RF_LINKML.curie('attr_description'),
                   model_uri=GEOCHEM_RF_LINKML.attr_description, domain=None, range=Optional[str])

slots.analysis_detection_limit = Slot(uri=GEOCHEM_RF_LINKML.analysis_detection_limit, name="analysis_detection_limit", curie=GEOCHEM_RF_LINKML.curie('analysis_detection_limit'),
                   model_uri=GEOCHEM_RF_LINKML.analysis_detection_limit, domain=None, range=Optional[float])

slots.analysis_precision = Slot(uri=GEOCHEM_RF_LINKML.analysis_precision, name="analysis_precision", curie=GEOCHEM_RF_LINKML.curie('analysis_precision'),
                   model_uri=GEOCHEM_RF_LINKML.analysis_precision, domain=None, range=Optional[float])

slots.instrument_precision = Slot(uri=GEOCHEM_RF_LINKML.instrument_precision, name="instrument_precision", curie=GEOCHEM_RF_LINKML.curie('instrument_precision'),
                   model_uri=GEOCHEM_RF_LINKML.instrument_precision, domain=None, range=Optional[float])

slots.method_instrument = Slot(uri=GEOCHEM_RF_LINKML.method_instrument, name="method_instrument", curie=GEOCHEM_RF_LINKML.curie('method_instrument'),
                   model_uri=GEOCHEM_RF_LINKML.method_instrument, domain=None, range=Optional[str])

slots.method_reference = Slot(uri=GEOCHEM_RF_LINKML.method_reference, name="method_reference", curie=GEOCHEM_RF_LINKML.curie('method_reference'),
                   model_uri=GEOCHEM_RF_LINKML.method_reference, domain=None, range=Optional[str])

slots.method_hold_time = Slot(uri=GEOCHEM_RF_LINKML.method_hold_time, name="method_hold_time", curie=GEOCHEM_RF_LINKML.curie('method_hold_time'),
                   model_uri=GEOCHEM_RF_LINKML.method_hold_time, domain=None, range=Optional[str])

slots.method_temp = Slot(uri=GEOCHEM_RF_LINKML.method_temp, name="method_temp", curie=GEOCHEM_RF_LINKML.curie('method_temp'),
                   model_uri=GEOCHEM_RF_LINKML.method_temp, domain=None, range=Optional[str])

slots.method_light = Slot(uri=GEOCHEM_RF_LINKML.method_light, name="method_light", curie=GEOCHEM_RF_LINKML.curie('method_light'),
                   model_uri=GEOCHEM_RF_LINKML.method_light, domain=None, range=Optional[str])

slots.method_atmosphere = Slot(uri=GEOCHEM_RF_LINKML.method_atmosphere, name="method_atmosphere", curie=GEOCHEM_RF_LINKML.curie('method_atmosphere'),
                   model_uri=GEOCHEM_RF_LINKML.method_atmosphere, domain=None, range=Optional[str])

slots.method_moisture = Slot(uri=GEOCHEM_RF_LINKML.method_moisture, name="method_moisture", curie=GEOCHEM_RF_LINKML.curie('method_moisture'),
                   model_uri=GEOCHEM_RF_LINKML.method_moisture, domain=None, range=Optional[str])

slots.method_medium = Slot(uri=GEOCHEM_RF_LINKML.method_medium, name="method_medium", curie=GEOCHEM_RF_LINKML.curie('method_medium'),
                   model_uri=GEOCHEM_RF_LINKML.method_medium, domain=None, range=Optional[str])

slots.method_time = Slot(uri=GEOCHEM_RF_LINKML.method_time, name="method_time", curie=GEOCHEM_RF_LINKML.curie('method_time'),
                   model_uri=GEOCHEM_RF_LINKML.method_time, domain=None, range=Optional[str])

slots.method_lab_contact = Slot(uri=GEOCHEM_RF_LINKML.method_lab_contact, name="method_lab_contact", curie=GEOCHEM_RF_LINKML.curie('method_lab_contact'),
                   model_uri=GEOCHEM_RF_LINKML.method_lab_contact, domain=None, range=Optional[str])

slots.method_instrument_operator = Slot(uri=GEOCHEM_RF_LINKML.method_instrument_operator, name="method_instrument_operator", curie=GEOCHEM_RF_LINKML.curie('method_instrument_operator'),
                   model_uri=GEOCHEM_RF_LINKML.method_instrument_operator, domain=None, range=Optional[str])

slots.method_lab = Slot(uri=GEOCHEM_RF_LINKML.method_lab, name="method_lab", curie=GEOCHEM_RF_LINKML.curie('method_lab'),
                   model_uri=GEOCHEM_RF_LINKML.method_lab, domain=None, range=Optional[str])

slots.sample = Slot(uri=GEOCHEM_RF_LINKML.sample, name="sample", curie=GEOCHEM_RF_LINKML.curie('sample'),
                   model_uri=GEOCHEM_RF_LINKML.sample, domain=None, range=Optional[Union[str, SampleSampleName]])

slots.variable = Slot(uri=GEOCHEM_RF_LINKML.variable, name="variable", curie=GEOCHEM_RF_LINKML.curie('variable'),
                   model_uri=GEOCHEM_RF_LINKML.variable, domain=None, range=Optional[Union[str, MeasurementVariableId]])

slots.method = Slot(uri=GEOCHEM_RF_LINKML.method, name="method", curie=GEOCHEM_RF_LINKML.curie('method'),
                   model_uri=GEOCHEM_RF_LINKML.method, domain=None, range=Optional[Union[str, MethodAttrId]])

slots.numeric_value = Slot(uri=NMDC.numeric_value, name="numeric_value", curie=NMDC.curie('numeric_value'),
                   model_uri=GEOCHEM_RF_LINKML.numeric_value, domain=None, range=Optional[float])

slots.string_value = Slot(uri=GEOCHEM_RF_LINKML.string_value, name="string_value", curie=GEOCHEM_RF_LINKML.curie('string_value'),
                   model_uri=GEOCHEM_RF_LINKML.string_value, domain=None, range=Optional[str])

slots.datetime_value = Slot(uri=GEOCHEM_RF_LINKML.datetime_value, name="datetime_value", curie=GEOCHEM_RF_LINKML.curie('datetime_value'),
                   model_uri=GEOCHEM_RF_LINKML.datetime_value, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.raw_value = Slot(uri=NMDC.raw_value, name="raw_value", curie=NMDC.curie('raw_value'),
                   model_uri=GEOCHEM_RF_LINKML.raw_value, domain=None, range=Optional[str])

slots.flag = Slot(uri=GEOCHEM_RF_LINKML.flag, name="flag", curie=GEOCHEM_RF_LINKML.curie('flag'),
                   model_uri=GEOCHEM_RF_LINKML.flag, domain=None, range=Optional[Union[str, list[str]]])

slots.treatment_id = Slot(uri=GEOCHEM_RF_LINKML.treatment_id, name="treatment_id", curie=GEOCHEM_RF_LINKML.curie('treatment_id'),
                   model_uri=GEOCHEM_RF_LINKML.treatment_id, domain=None, range=Optional[str])

slots.datetime_measured = Slot(uri=GEOCHEM_RF_LINKML.datetime_measured, name="datetime_measured", curie=GEOCHEM_RF_LINKML.curie('datetime_measured'),
                   model_uri=GEOCHEM_RF_LINKML.datetime_measured, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.time_elapsed = Slot(uri=GEOCHEM_RF_LINKML.time_elapsed, name="time_elapsed", curie=GEOCHEM_RF_LINKML.curie('time_elapsed'),
                   model_uri=GEOCHEM_RF_LINKML.time_elapsed, domain=None, range=Optional[float])

slots.measurements = Slot(uri=GEOCHEM_RF_LINKML.measurements, name="measurements", curie=GEOCHEM_RF_LINKML.curie('measurements'),
                   model_uri=GEOCHEM_RF_LINKML.measurements, domain=None, range=Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]])

slots.variables = Slot(uri=GEOCHEM_RF_LINKML.variables, name="variables", curie=GEOCHEM_RF_LINKML.curie('variables'),
                   model_uri=GEOCHEM_RF_LINKML.variables, domain=None, range=Optional[Union[dict[Union[str, MeasurementVariableId], Union[dict, MeasurementVariable]], list[Union[dict, MeasurementVariable]]]])

slots.samples = Slot(uri=GEOCHEM_RF_LINKML.samples, name="samples", curie=GEOCHEM_RF_LINKML.curie('samples'),
                   model_uri=GEOCHEM_RF_LINKML.samples, domain=None, range=Optional[Union[dict[Union[str, SampleSampleName], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.methods = Slot(uri=GEOCHEM_RF_LINKML.methods, name="methods", curie=GEOCHEM_RF_LINKML.curie('methods'),
                   model_uri=GEOCHEM_RF_LINKML.methods, domain=None, range=Optional[Union[dict[Union[str, MethodAttrId], Union[dict, Method]], list[Union[dict, Method]]]])

slots.MeasurementVariable_id = Slot(uri=SCHEMA.identifier, name="MeasurementVariable_id", curie=SCHEMA.curie('identifier'),
                   model_uri=GEOCHEM_RF_LINKML.MeasurementVariable_id, domain=MeasurementVariable, range=Union[str, MeasurementVariableId])

slots.MeasurementVariable_unit = Slot(uri=GEOCHEM_RF_LINKML.unit, name="MeasurementVariable_unit", curie=GEOCHEM_RF_LINKML.curie('unit'),
                   model_uri=GEOCHEM_RF_LINKML.MeasurementVariable_unit, domain=MeasurementVariable, range=Union[str, "UnitEnum"])

slots.MeasurementVariable_definition = Slot(uri=SCHEMA.description, name="MeasurementVariable_definition", curie=SCHEMA.curie('description'),
                   model_uri=GEOCHEM_RF_LINKML.MeasurementVariable_definition, domain=MeasurementVariable, range=str)

slots.Sample_sample_name = Slot(uri=GEOCHEM_RF_LINKML.sample_name, name="Sample_sample_name", curie=GEOCHEM_RF_LINKML.curie('sample_name'),
                   model_uri=GEOCHEM_RF_LINKML.Sample_sample_name, domain=Sample, range=Union[str, SampleSampleName])

slots.Method_attr_id = Slot(uri=GEOCHEM_RF_LINKML.attr_id, name="Method_attr_id", curie=GEOCHEM_RF_LINKML.curie('attr_id'),
                   model_uri=GEOCHEM_RF_LINKML.Method_attr_id, domain=Method, range=Union[str, MethodAttrId])

slots.Method_attr_type = Slot(uri=GEOCHEM_RF_LINKML.attr_type, name="Method_attr_type", curie=GEOCHEM_RF_LINKML.curie('attr_type'),
                   model_uri=GEOCHEM_RF_LINKML.Method_attr_type, domain=Method, range=Union[str, "AttrTypeEnum"])

slots.Method_attr_description = Slot(uri=GEOCHEM_RF_LINKML.attr_description, name="Method_attr_description", curie=GEOCHEM_RF_LINKML.curie('attr_description'),
                   model_uri=GEOCHEM_RF_LINKML.Method_attr_description, domain=Method, range=str)

slots.Measurement_sample = Slot(uri=GEOCHEM_RF_LINKML.sample, name="Measurement_sample", curie=GEOCHEM_RF_LINKML.curie('sample'),
                   model_uri=GEOCHEM_RF_LINKML.Measurement_sample, domain=Measurement, range=Union[str, SampleSampleName])

slots.Measurement_variable = Slot(uri=GEOCHEM_RF_LINKML.variable, name="Measurement_variable", curie=GEOCHEM_RF_LINKML.curie('variable'),
                   model_uri=GEOCHEM_RF_LINKML.Measurement_variable, domain=Measurement, range=Union[str, MeasurementVariableId])

slots.Measurement_method = Slot(uri=GEOCHEM_RF_LINKML.method, name="Measurement_method", curie=GEOCHEM_RF_LINKML.curie('method'),
                   model_uri=GEOCHEM_RF_LINKML.Measurement_method, domain=Measurement, range=Optional[Union[Union[str, MethodAttrId], list[Union[str, MethodAttrId]]]])

slots.Measurement_numeric_value = Slot(uri=NMDC.numeric_value, name="Measurement_numeric_value", curie=NMDC.curie('numeric_value'),
                   model_uri=GEOCHEM_RF_LINKML.Measurement_numeric_value, domain=Measurement, range=Optional[float])

slots.Dataset_measurements = Slot(uri=GEOCHEM_RF_LINKML.measurements, name="Dataset_measurements", curie=GEOCHEM_RF_LINKML.curie('measurements'),
                   model_uri=GEOCHEM_RF_LINKML.Dataset_measurements, domain=Dataset, range=Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]])

slots.Dataset_variables = Slot(uri=GEOCHEM_RF_LINKML.variables, name="Dataset_variables", curie=GEOCHEM_RF_LINKML.curie('variables'),
                   model_uri=GEOCHEM_RF_LINKML.Dataset_variables, domain=Dataset, range=Optional[Union[dict[Union[str, MeasurementVariableId], Union[dict, MeasurementVariable]], list[Union[dict, MeasurementVariable]]]])

slots.Dataset_samples = Slot(uri=GEOCHEM_RF_LINKML.samples, name="Dataset_samples", curie=GEOCHEM_RF_LINKML.curie('samples'),
                   model_uri=GEOCHEM_RF_LINKML.Dataset_samples, domain=Dataset, range=Optional[Union[dict[Union[str, SampleSampleName], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.Dataset_methods = Slot(uri=GEOCHEM_RF_LINKML.methods, name="Dataset_methods", curie=GEOCHEM_RF_LINKML.curie('methods'),
                   model_uri=GEOCHEM_RF_LINKML.Dataset_methods, domain=Dataset, range=Optional[Union[dict[Union[str, MethodAttrId], Union[dict, Method]], list[Union[dict, Method]]]])

