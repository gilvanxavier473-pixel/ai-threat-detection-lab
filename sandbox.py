DANGEROUS_COMMANDS = ["rm", "sudo", "shutdown", "reboot", "mkfs"]

def safe_execute(command: str) -> dict:
    command_lower = command.lower()

    for dangerous in DANGEROUS_COMMANDS:
        if dangerous in command_lower:
            return {"allowed": False, "message": "Comando bloqueado pelo sandbox."}

    return {"allowed": True, "message": "Comando aprovado apenas para simulação."}
