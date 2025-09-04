# Setting up OpenWebUI with n8n


## n8n setup

1. Add **Webhook** node as input:
    - *HTTP Method* = *POST*
    - *Respond* = *Using ‘Respond to Webhook’ Node*
2. Add **Response to Webhook** node as output
3. Copy *Webhook URLs > Production URL*
4. Activate the workflow


## Open WebUI setup

1. *Admin Panel > Functions > Create > New Function*
2. Set title, description and paste and paste the code from [n8n_pipe.py](n8n_pipe.py)
3. *Valves > N8N Url* = (Paste Production URL from previous step 3.and replace `localhost` with `n8n`)
4. Enable


## Use

Access Open WebUI at [http://localhost:3000/](http://localhost:3000/)


## Tips

If you use **When chat message received** and **Webhook** nodes as inputs to your workflow, parameters will come from `$json` and `$json.body` respectively.

To support both for instance in an **AI Agent** node:
- *Source for Prompt (User Message)* = *Define below*
- *Prompt (User Message)* = `{{ $json?.chatInput || $json?.body.chatInput }}`

Analogously for a memory node:

- *Session ID* = *Define below*
- *Key* = `{{ $json?.sessionId || $json?.body.sessionId }}`

It's more convenient to simply use connect both input nodes to an **Edit Fields (Set)** node unifying under new fields, e.g.:
- `chatInput` = `{{ $json?.chatInput || $json?.body.chatInput }}`
- `sessionId` = `{{ $json?.sessionId || $json?.body.sessionId }}`


## Credits

- [n8n_pipe.py](https://github.com/coleam00/ai-agents-masterclass/blob/main/local-ai-packaged/n8n_pipe.py)
