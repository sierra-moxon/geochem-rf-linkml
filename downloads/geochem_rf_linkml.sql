-- # Class: Attribute Description: A domain, measurement, attribute, property, or descriptor for something measured. The identity of *what* is measured (the "bare concept", e.g. `temperature`). Mirrors the BERtron/NMDC Attribute pattern: a thin data-dictionary anchor whose `id` is a controlled-vocabulary CURIE.
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: label Description: Human-readable label for the attribute. Where available, the term name from the controlled vocabulary (CUAHSI/ODM2/BERVO).
-- # Class: MeasurementVariable Description: A fully-qualified measured variable: the bare `Attribute` concept plus its unit and statistical/temporal qualifiers. One row of the ESS-DIVE Data Dictionary. This is the "variable dimension" of the star schema; the dimension business key is the qualified-identity tuple (see `unique_keys`), NOT the arbitrary user column name.
--     * Slot: unit Description: UCUM-coded unit of the measurement (Data Dictionary `unit`).
--     * Slot: unit_cv_id Description: The unit expressed as an ontology CURIE (e.g. UO / UCUM).
--     * Slot: definition Description: Definition of the measured variable (Data Dictionary `definition`).
--     * Slot: data_type Description: Data type of the values (Data Dictionary `data_type`).
--     * Slot: unit_basis Description: Basis for the reported unit (e.g. dry weight), Data Dictionary `unit_basis`.
--     * Slot: missing_value_code Description: Code used in the data file to indicate a missing value.
--     * Slot: statistic_measurement Description: Statistic applied across measurements (Data Dictionary `statistic_measurement`).
--     * Slot: statistic_spatial Description: Statistic applied across space (Data Dictionary `statistic_spatial`).
--     * Slot: statistic_temporal Description: Statistic applied across time (Data Dictionary `statistic_temporal`).
--     * Slot: representation_temporal Description: Temporal representation / interval (Data Dictionary `representation_temporal`).
--     * Slot: lower_bound Description: Lower plausibility/validity bound for the value.
--     * Slot: upper_bound Description: Upper plausibility/validity bound for the value.
--     * Slot: column_or_row_name Description: The arbitrary user-supplied column (or row) label from the source data file. NOT an identity -- kept only as a non-identifying alias.
--     * Slot: column_or_row_long_name Description: Optional long-form name for the column/row.
--     * Slot: id Description: CURIE for the qualified variable (or its underlying CUAHSI/ODM2/BERVO term). Serves as the dimension key / foreign-key target.
--     * Slot: label Description: Human-readable label for the attribute. Where available, the term name from the controlled vocabulary (CUAHSI/ODM2/BERVO).
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: Sample Description: A physical sample (or a time point on a sample) that measurements are made on. The sample dimension of the star schema.
--     * Slot: sample_name Description: Name/identifier of the physical sample.
--     * Slot: datetime_collected Description: Date/time the sample was collected.
--     * Slot: latitude Description: Latitude (WGS84 decimal degrees).
--     * Slot: longitude Description: Longitude (WGS84 decimal degrees).
--     * Slot: location_description Description: Free-text description of the sampling location.
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: Method Description: One row of the Full "Methods & Attributes" file (`*_sample_attr.csv`): the method/flag/treatment/sensor definition referenced per-measurement.
--     * Slot: attr_id Description: Identifier for a method/flag/treatment/sensor (Methods & Attributes `attr_id`).
--     * Slot: attr_type Description: Kind of attribute identified by `attr_id`.
--     * Slot: attr_description Description: Description of the method/flag/treatment/sensor.
--     * Slot: analysis_detection_limit Description: Analysis detection limit.
--     * Slot: analysis_precision Description: Analysis precision.
--     * Slot: instrument_precision Description: Instrument precision.
--     * Slot: lower_bound Description: Lower plausibility/validity bound for the value.
--     * Slot: upper_bound Description: Upper plausibility/validity bound for the value.
--     * Slot: method_instrument Description: Instrument used.
--     * Slot: method_reference Description: Citation/reference for the method.
--     * Slot: method_hold_time Description: Sample hold time before analysis.
--     * Slot: method_temp Description: Temperature condition of the method.
--     * Slot: method_light Description: Light condition of the method.
--     * Slot: method_atmosphere Description: Atmospheric condition of the method.
--     * Slot: method_moisture Description: Moisture condition of the method.
--     * Slot: method_medium Description: Medium of the method.
--     * Slot: method_time Description: Timing detail of the method.
--     * Slot: method_lab_contact Description: Laboratory contact.
--     * Slot: method_instrument_operator Description: Instrument operator.
--     * Slot: method_lab Description: Laboratory that performed the analysis.
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: Measurement Description: A single measured value: the "fact" of the star schema. Points at a `Sample` and a `MeasurementVariable` (and optionally a `Method`) by identifier, and carries the actual measure(s).
--     * Slot: id
--     * Slot: sample Description: Foreign key to the sample dimension.
--     * Slot: variable Description: Foreign key to the variable dimension.
--     * Slot: numeric_value Description: The numeric measure (kept typed for Parquet stats / pushdown).
--     * Slot: string_value Description: The measure when it is textual (typed EAV column, sparse).
--     * Slot: datetime_value Description: The measure when it is a date/time (typed EAV column, sparse).
--     * Slot: raw_value Description: The unnormalized atomic string as reported (e.g. "2.2 mg/L").
--     * Slot: treatment_id Description: Treatment identifier applied to this measurement.
--     * Slot: datetime_measured Description: Date/time the measurement was made.
--     * Slot: time_elapsed Description: Elapsed time for a time-series measurement.
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: Dataset Description: A single ESS-DIVE sample-data package: the whole `Measurement` fact table plus the `MeasurementVariable` data-dictionary dimension (and the sample / method dimensions).
--     * Slot: id Description: A unique identifier for a thing.
--     * Slot: name Description: A human-readable name for a thing.
-- # Class: Measurement_method
--     * Slot: Measurement_id Description: Autocreated FK slot
--     * Slot: method_attr_id Description: Foreign key to the method dimension (Full RF).
-- # Class: Measurement_flag
--     * Slot: Measurement_id Description: Autocreated FK slot
--     * Slot: flag Description: Quality/other flags for the measurement (`{...}_flag`).

CREATE TABLE "Attribute" (
	id TEXT NOT NULL,
	label TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Attribute_id" ON "Attribute" (id);

CREATE TABLE "Dataset" (
	id TEXT NOT NULL,
	name TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);

CREATE TABLE "MeasurementVariable" (
	unit VARCHAR(27) NOT NULL,
	unit_cv_id TEXT,
	definition TEXT NOT NULL,
	data_type VARCHAR(8),
	unit_basis TEXT,
	missing_value_code TEXT,
	statistic_measurement VARCHAR(23),
	statistic_spatial VARCHAR(23),
	statistic_temporal VARCHAR(23),
	representation_temporal VARCHAR(9),
	lower_bound FLOAT,
	upper_bound FLOAT,
	column_or_row_name TEXT,
	column_or_row_long_name TEXT,
	id TEXT NOT NULL,
	label TEXT NOT NULL,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	UNIQUE (label, unit, unit_basis, statistic_measurement, statistic_spatial, statistic_temporal, representation_temporal),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_MeasurementVariable_id" ON "MeasurementVariable" (id);
CREATE INDEX "MeasurementVariable_label_unit_unit_basis_statistic_measurement_statistic_spatial_statistic_temporal_representation_temporal_idx" ON "MeasurementVariable" (label, unit, unit_basis, statistic_measurement, statistic_spatial, statistic_temporal, representation_temporal);

CREATE TABLE "Sample" (
	sample_name TEXT NOT NULL,
	datetime_collected DATETIME,
	latitude FLOAT,
	longitude FLOAT,
	location_description TEXT,
	"Dataset_id" TEXT,
	PRIMARY KEY (sample_name),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Sample_sample_name" ON "Sample" (sample_name);

CREATE TABLE "Method" (
	attr_id TEXT NOT NULL,
	attr_type VARCHAR(12) NOT NULL,
	attr_description TEXT NOT NULL,
	analysis_detection_limit FLOAT,
	analysis_precision FLOAT,
	instrument_precision FLOAT,
	lower_bound FLOAT,
	upper_bound FLOAT,
	method_instrument TEXT,
	method_reference TEXT,
	method_hold_time TEXT,
	method_temp TEXT,
	method_light TEXT,
	method_atmosphere TEXT,
	method_moisture TEXT,
	method_medium TEXT,
	method_time TEXT,
	method_lab_contact TEXT,
	method_instrument_operator TEXT,
	method_lab TEXT,
	"Dataset_id" TEXT,
	PRIMARY KEY (attr_id),
	UNIQUE (attr_id, attr_type),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "Method_attr_id_attr_type_idx" ON "Method" (attr_id, attr_type);
CREATE INDEX "ix_Method_attr_id" ON "Method" (attr_id);

CREATE TABLE "Measurement" (
	id INTEGER NOT NULL,
	sample TEXT NOT NULL,
	variable TEXT NOT NULL,
	numeric_value FLOAT,
	string_value TEXT,
	datetime_value DATETIME,
	raw_value TEXT,
	treatment_id TEXT,
	datetime_measured DATETIME,
	time_elapsed FLOAT,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(sample) REFERENCES "Sample" (sample_name),
	FOREIGN KEY(variable) REFERENCES "MeasurementVariable" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);
CREATE INDEX "ix_Measurement_id" ON "Measurement" (id);

CREATE TABLE "Measurement_method" (
	"Measurement_id" INTEGER,
	method_attr_id TEXT,
	PRIMARY KEY ("Measurement_id", method_attr_id),
	FOREIGN KEY("Measurement_id") REFERENCES "Measurement" (id),
	FOREIGN KEY(method_attr_id) REFERENCES "Method" (attr_id)
);
CREATE INDEX "ix_Measurement_method_method_attr_id" ON "Measurement_method" (method_attr_id);
CREATE INDEX "ix_Measurement_method_Measurement_id" ON "Measurement_method" ("Measurement_id");

CREATE TABLE "Measurement_flag" (
	"Measurement_id" INTEGER,
	flag TEXT,
	PRIMARY KEY ("Measurement_id", flag),
	FOREIGN KEY("Measurement_id") REFERENCES "Measurement" (id)
);
CREATE INDEX "ix_Measurement_flag_Measurement_id" ON "Measurement_flag" ("Measurement_id");
CREATE INDEX "ix_Measurement_flag_flag" ON "Measurement_flag" (flag);
