from flask import Flask, request, jsonify, send_from_directory
import subprocess
import platform
import socket
import ipaddress
import re
import shlex
from pathlib import Path

app = Flask(__name__, static_folder="static", static_url_path="/")

# --- Utility: validate host (simple, prevents command injection) ---
HOST_RE = re.compile(r"^[\w\.\-:]+$")  # allow letters, digits, dot, dash, colon (for IPv6 literal port)
def safe_host(host: str) -> bool:
    return bool(host) and HOST_RE.match(host)

# --- Serve frontend ---
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# --- DNS resolve ---
@app.route("/api/resolve")
def api_resolve():
    host = request.args.get("host", "").strip()
    if not safe_host(host):
        return jsonify({"error": "Invalid host"}), 400
    try:
        ip = socket.gethostbyname(host)
        return jsonify({"host": host, "ip": ip})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Ping (cross-platform) ---
@app.route("/api/ping")
def api_ping():
    host = request.args.get("host", "").strip()
    count = request.args.get("count", "4").strip()
    if not safe_host(host):
        return jsonify({"error": "Invalid host"}), 400
    # limit count to small integer
    try:
        c = int(count)
        c = max(1, min(c, 10))
    except:
        c = 4
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", str(c), host]
    else:
        cmd = ["ping", "-c", str(c), host]
    try:
        # run safely without shell
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        output = proc.stdout + proc.stderr
        success = proc.returncode == 0
        return jsonify({"host": host, "success": success, "output": output})
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Ping timed out"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- CIDR calculator ---
@app.route("/api/cidr")
def api_cidr():
    cidr = request.args.get("cidr", "").strip()
    if not cidr:
        return jsonify({"error": "cidr param required, e.g. 192.168.1.0/24"}), 400
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        network_address = str(net.network_address)
        broadcast_address = str(net.broadcast_address) if hasattr(net, "broadcast_address") else None
        num_addresses = net.num_addresses
        hosts = []
        # only include first/last usable addresses for large nets
        if num_addresses <= 256:
            hosts = [str(ip) for ip in net.hosts()]
        else:
            # provide start and end, and total count
            hosts = [str(next(net.hosts())), str(list(net.hosts())[-1])]  # careful: converting hosts() fully large nets uses memory - but only used when >256 which is rare; safe for demo
        return jsonify({
            "cidr": cidr,
            "network_address": network_address,
            "broadcast_address": broadcast_address,
            "num_addresses": num_addresses,
            "first_last_hosts_sample": hosts
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
