import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

//Agregar este archivo dentro de una carpeta llamada Simulation antes de ejecutar
class MySimulation extends Simulation {

  val httpConf = http
    .baseUrl("http://localhost:5000") //Url de la app Flask, por default esta en este puerto
    .acceptHeader("application/json")

  val scn = scenario("Enviar JSON a Flask")
    .exec(http("POST JSON")
      .post("/") //Se cambia por la ruta que se definio en flask
      .body(StringBody("""{
        "animales": [
          {
            "Tipo": "Perro",
            "Nombre": "Max"
          },
          {
            "Tipo": "Gato",
            "Nombre": "Manchas"
          },
          {
            "Tipo": "Perro",
            "Nombre": "Bruno"
          }
        ]
      }""")).asJson  //Todo ese texto es el JSON que se va a enviar, se puede modificar para hacerlo como se desee
      .check(status.is(200)))

  setUp(
    scn.inject(
      constantUsersPerSec(1) during (1 seconds) //Cantidad de usuarios por segundo que van a realizar peticiones
    )
  ).protocols(httpConf)

}