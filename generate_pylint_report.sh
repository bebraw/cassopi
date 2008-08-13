pylint --rcfile=pylint_config cassopi > cassopi_log.html
./dottopng.sh import_graph
./dottopng.sh ext_import_graph
./dottopng.sh int_import_graph
