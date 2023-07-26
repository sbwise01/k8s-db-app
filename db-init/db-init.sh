#!/usr/bin/env bash

echo "Running database init scripts"
psql -h $PGHOST -p $PGPORT -d $PGDATABASE -U $PGUSER -f create.sql

echo "waiting for it to finish"
sleep 120

echo "Completed database init"
