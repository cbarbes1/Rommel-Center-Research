from GeneralUtilities.tracing.tracer import trace

@trace(log_file="/mnt/linuxlab/home/cbarbes1/Rommel-Center-Research/traces.txt", level="INFO")
def add (a, b):
    if (a == b):
        return a+b
    else:
        raise Exception("Intentional Error")

if __name__ == "__main__":
    add(5, 5)
    add(5, 4)

    
