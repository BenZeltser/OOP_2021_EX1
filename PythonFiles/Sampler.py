import ElevatorAlgo
import ElevatorAlgo
import Building
a = [12,12,12,12]
building = Building.buildingUnit(1, 2, a)
algo = ElevatorAlgo.elevatorAlgo(building)
algo.getUpElevators(building)
algo.getDownElevators(building)