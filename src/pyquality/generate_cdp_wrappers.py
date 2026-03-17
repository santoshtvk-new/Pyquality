import urllib.request
import json
import os

URL = "https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/browser_protocol.json"

def generate_python_class(domain_data):
    domain_name = domain_data['domain']
    commands = domain_data.get('commands', [])
    
    code = f"class {domain_name}Domain:\n"
    code += f"    def __init__(self, driver):\n"
    code += f"        self.driver = driver\n\n"
    
    for cmd in commands:
        cmd_name = cmd['name']
        description = cmd.get('description', f"Call {domain_name}.{cmd_name}").replace('\n', ' ')
        parameters = cmd.get('parameters', [])
        
        args = ["self"]
        kwargs = []
        doc_params = []
        
        for p in parameters:
            p_name = p['name']
            # Make sure it's a valid python identifier, e.g., avoid `type`
            safe_p_name = p_name if p_name not in ['type', 'id', 'class'] else p_name + "_"
            
            if p.get('optional'):
                kwargs.append(f"{safe_p_name}=None")
            else:
                args.append(safe_p_name)
            
            doc_params.append(f"{p_name} ({p.get('type', 'any')}): {p.get('description', '')}")
            
        py_args_str = ", ".join(args + kwargs)
        
        # Build the python method
        code += f"    def {cmd_name}({py_args_str}):\n"
        code += f'        """\n        {description}\n'
        if doc_params:
            for dp in doc_params:
                code += f"        - {dp}\n"
        code += f'        """\n'
        
        code += f'        params = {{}}\n'
        for p in parameters:
            p_name = p['name']
            safe_p_name = p_name if p_name not in ['type', 'id', 'class'] else p_name + "_"
            if p.get('optional'):
                code += f'        if {safe_p_name} is not None:\n'
                code += f'            params["{p_name}"] = {safe_p_name}\n'
            else:
                code += f'        params["{p_name}"] = {safe_p_name}\n'
                
        code += f'        return self.driver.execute_and_wait("{domain_name}.{cmd_name}", params)\n\n'
        
    return code

def main():
    print("Fetching protocol...")
    req = urllib.request.urlopen(URL)
    data = json.loads(req.read())
    
    output_dir = os.path.join(os.path.dirname(__file__), "domains")
    os.makedirs(output_dir, exist_ok=True)
    
    init_file = os.path.join(output_dir, "__init__.py")
    with open(init_file, "w", encoding="utf-8") as f:
        f.write("# Auto-generated CDP Domains\n")
    
    for domain in data['domains']:
        print(f"Generating {domain['domain']} wrapper...")
        code = generate_python_class(domain)
        file_path = os.path.join(output_dir, f"{domain['domain'].lower()}.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
            
        with open(init_file, "a", encoding="utf-8") as f:
            f.write(f"from .{domain['domain'].lower()} import {domain['domain']}Domain\n")

if __name__ == "__main__":
    main()
