extends CanvasLayer

func _ready():
	$Timer.start()
	$HTTPRequest.connect("request_completed", self, "_on_request_completed")

func _on_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	$scene.translation = Vector3(json.result[0][0], json.result[0][1], json.result[0][2])
	print(json.result)


func _on_Timer_timeout():
 $HTTPRequest.request("http://10.254.17.145:3000/criar")
