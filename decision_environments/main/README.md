```shell
ansible-builder build -f decision-environment.yml \
-t aap-toolbox-de:latest --build-arg "--arch x86_64" \
--no-cache

podman tag localhost/aap-toolbox-de:latest \
quay.io/rywillia/aap-toolbox-de:latest

podman push quay.io/rywillia/aap-toolbox-de:latest
```
