#!/bin/bash
psql -U admin

psql CREATE DATABASE ssluzba;
psql CREATE TABLE IF NOT EXISTS public.users (jmbg character(13)[], name text, user_type text, PRIMARY KEY (jmbg, user_type));

EOSQL