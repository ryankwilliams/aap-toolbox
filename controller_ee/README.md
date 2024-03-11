```shell
ansible-builder build -f execution-environment.yml \
-t aap-toolbox-ee:latest --build-arg "--arch x86_64" \
--no-cache

podman tag localhost/aap-toolbox-ee:latest \
quay.io/rywillia/aap-toolbox-ee:latest

podman push quay.io/rywillia/aap-toolbox-ee:latest
```
