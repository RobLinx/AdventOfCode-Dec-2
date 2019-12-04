import replit;
import math;

fileName = "input.txt";
replit.clear();

def processInput(pointer):
  hiPtr = len(memory) - 1
  opCode = memory[pointer]
  opPtr1 = memory[pointer+1]
  opPtr2 = memory[pointer+2]
  dstPtr = memory[pointer+3]

  #print(opCode,hiPtr,pointer,opPtr1,opPtr2,dstPtr, sep=',')
  if ((dstPtr > hiPtr) or (opPtr1 > hiPtr) or (opPtr2 > hiPtr)):
    return "ERROR"

  op1 = memory[opPtr1]
  op2 = memory[opPtr2]
  val = int
  ret = str

  if opCode == 1:
    val = op1 + op2
    ret = "CONTINUE"
  elif opCode == 2:
    val = op1 * op2
    ret = "CONTINUE"
  elif opCode == 99:
    ret = "HALT"
  else:
    ret = "ERROR"

  if ret == "CONTINUE":
    memory[dstPtr] = val

  return ret

def processNounVerb(noun, verb):

  #print(memory[1], memory[2], sep=',')
  memory[1] = noun
  memory[2] = verb

  pointer = 0
  while True:
    #print(".",end='')
    retVal = processInput(pointer);
    if (retVal == "HALT") or (retVal == "ERROR"):
      #print("HALTING",retVal)
      break;
    pointer += 4;
    if pointer > len(memory):
      #print("MEMORY")
      break;

  if memory[0] == desiredOutput:
    return "SUCCESS"
  else:
    return "TRYAGAIN: " + str(memory[0])

# initial file read
inputFile = open(fileName)
inputString = inputFile.read()
inputArray = list()
inputArray = [int(x) for x in inputString.split(",")]
memory = inputArray

desiredOutput = 19690720

foundIt = False
for noun in range(0,164):
  if foundIt: break
  for verb in range(0,164):
    if foundIt: break
    print("Trying: " + str(noun) + ", " + str(verb))
    memory = [int(x) for x in inputString.split(",")]
    retVal = processNounVerb(noun, verb)
    if retVal == "SUCCESS":
      print("Yay! " + str(100 * noun + verb))
      foundIt = True
      break
    else:
      print(retVal)


