# agent
Different take on a tool-calling agent...starting from the ground up with a simpler llama-cpp version using Qwen2.5-Coder

## Invoking the server to run:
```
llama-server.exe -m .\Qwen2.5-Coder-3B-Q4_K_M.gguf --ctx-size 4096 --port 8080 -ngl 99 --batch-size 256 --chat-template qwen -fa on --jinja
```

---
Models are currently housed in ~/models
