-- Table: public.contatos

-- DROP TABLE IF EXISTS public.contatos;

CREATE TABLE IF NOT EXISTS public.contatos
(
    id_contato integer NOT NULL DEFAULT nextval('contatos_id_contato_seq'::regclass),
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    telefone character varying(11) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT contatos_pkey PRIMARY KEY (id_contato)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.contatos
    OWNER to postgres;