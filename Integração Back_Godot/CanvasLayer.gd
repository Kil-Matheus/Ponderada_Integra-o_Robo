extends CanvasLayer

#Função de partida, onde a cada espaço de tempo, será feito um requisição
func _ready():
	$Timer.start()
	$HTTPRequest.connect("request_completed", self, "_on_request_completed")

#Se a requisição conseguir algum valor, ele será mostrado no cosole as coordenadas, e as mesmas serão enviadas para o objeto
func _on_request_completed(result, response_code, headers, body):
	var json = JSON.parse(body.get_string_from_utf8())
	$scene.translation = Vector3(json.result[0][0], json.result[0][1], json.result[0][2])
	print(json.result)

#A cada espaço de tempo, será feito uma requisição nesse endereço específico. Endereço em que a nossa aplicação no Backend está rodando.
func _on_Timer_timeout():
 $HTTPRequest.request("http://127.0.0.1:3000/criar")
